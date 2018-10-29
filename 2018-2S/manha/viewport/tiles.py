'''
Created on 30/10/2014

@author: Aluno
'''
import pygame
from pygame.rect import Rect
from pygame.surface import Surface

class Conversao(object):
    def __init__(self, ratio):
        self.ratio = ratio
        
    def getWorldToPixels(self, pos):
        px = pos[0] * self.ratio[0]
        py = pos[1] * self.ratio[1]
        return (px, py)
    
    def getPixelsToWorld(self, pos):
        wx = pos[0] / self.ratio[0]
        wy = pos[1] / self.ratio[1]
        return (wx, wy)

    def getPixelsToWorldGap(self, pos):
        gx = pos[0] % self.ratio[0]
        gy = pos[1] % self.ratio[1]
        return (gx, gy)


class TileSet(object):
    def __init__(self, jsonObj):
        self.name = jsonObj['name']
        self.firstgid = jsonObj['firstgid']
        self.image_width = jsonObj['imagewidth']
        self.image_height = jsonObj['imageheight']
        self.tile_width = jsonObj['tilewidth']
        self.tile_height = jsonObj['tileheight']
        self.margin = jsonObj['margin']
        self.spacing = jsonObj['spacing']
        self.tileoffset = jsonObj['tileoffset']
        self.columns = self.image_width / self.tile_width
        self.lines = self.image_height / self.tile_height
        self.image = pygame.image.load(jsonObj['image'])
        self.lastgid = self.firstgid - 1 + (self.columns * self.lines)
        print("TileSet : ", self.name, " carregado...")

    def getTileByGId(self, gId):
        currentFrame = (gId - self.firstgid)
        column = currentFrame % self.columns
        line = currentFrame / self.columns
        x = self.margin + ( (self.tile_width + self.tileoffset["x"] ) * column)
        y = self.spacing + ( (self.tile_height  + self.tileoffset["y"] ) * line )
        w = self.tile_width
        h = self.tile_height
        r = Rect( (x, y), (w, h) )
        image = self.image.subsurface( r )
        brick = Brick( self, image, gId )
        return brick
      
    

class Brick():
    def __init__(self, tileset, imagem, gId):
        self.tileset = tileset
        self.image = imagem
        self.gId = gId  
        self.coluna = (gId - 1) % self.tileset.columns
        self.linha = (gId - 1) / self.tileset.columns   
        self.rect = Rect( (0,0), (imagem.get_width(), imagem.get_height()))  
        
        
class Layer( object ):
    def __init__(self, json):
        self.name = json['name']
        self.type = json['type']
        self.width = json['width']
        self.height = json['height']
        self.visible = json['visible']
        self.opacity = json['opacity']
        self.__data = json['data']
        self.internal_structure = []
        self.conversion = Conversao( (32, 32) )
        
        
    def prepare(self, tile_set):
        self.internal_structure = []
        for l in range(self.height):
            celulas = []
            for c in range(self.width):
                gid = self.__data[(l * self.width) + c]
                brk = Brick( tile_set, Surface( (32, 32), 0, 32), 0) 
                if (gid > 0):               
                    brk = tile_set.getTileByGId(gid)
                celulas.append( brk )
            self.internal_structure.append(celulas)


    def getFrame(self, c1, l1, c2, l2):
        cols = abs(c2 - c1)
        rows = abs(l2 - l1)        
        img = pygame.Surface( self.conversion.getWorldToPixels( (cols, rows) ), 0, 32 )
        for l in range( rows ):
            for c in range ( cols ):
                b = self.internal_structure[l + l1][c + c1]
                pos = self.conversion.getWorldToPixels( (c, l) )
                
                img.blit( b.image, pos )
        return img

                
    def getFrameRect(self, r):
        (c1, l1) = self.conversion.getPixelsToWorld( r.topleft )
        (c2, l2) = self.conversion.getPixelsToWorld( r.bottomright )
        img = self.getFrame(c1, l1, c2 + 1, l2 + 1)
        gapTop = self.conversion.getPixelsToWorldGap( r.topleft )
        imgFinal = img.subsurface( Rect( gapTop, r.size ) )
        return imgFinal
