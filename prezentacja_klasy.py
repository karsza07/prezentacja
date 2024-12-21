import pygame
from math import sqrt
import sys
import os
pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def draw_hex(screen, colour, a, x,y ):
    h = a*sqrt(3)/2
    x += a
    y += h
    points = [
        (x - a, y),
        (x - a / 2, y + h),
        (x + a / 2, y + h),
        (x + a, y),
        (x + a / 2, y - h),
        (x - a / 2, y - h),   
    ]
    pygame.draw.polygon(screen, colour, points)
    
def split_text(screen, font, color, text_name, space, x, y): # tekst to zmienna z przypisanym obietkem txt
    text = open(resource_path(text_name), "r", encoding = "utf-8")
    lista = text.read().splitlines()
    for i in lista:
        line = font.render(i, True, color)
        screen.blit(line, (x, y))
        y += space

def transform_image(screen, name, scale, xy):
    image = pygame.image.load(resource_path(name))
    image = pygame.transform.smoothscale(image, scale)
    screen.blit(image, xy)

def repeatable_slides(self, screen, ikona, text_name, photo):
    draw_hex(screen, (57, 41, 109), 904.5, -873.3, -9.7)
    line = self.font.render("Zastosowania VR", True, (0, 0, 0))
    screen.blit(line, (749.3, 22.9))
    split_text(screen, self.font_40, (232, 226, 226), text_name, 48.3, 31.6, 170)
    transform_image(screen, ikona, (120, 107), (31.6, 22))
    transform_image(screen, photo, (528.6, 457.7), (785, 155))

def zakladka(screen):
    rectangle = pygame.Rect((0, 0), (476.7, 159.4))
    pygame.draw.rect(screen, (57, 41, 109), rectangle)
    draw_hex(screen, (91, 85, 159), 183, 281.7, -157.8)
    draw_hex(screen, (83, 67, 137), 183, 242.6, -157.8)
    draw_hex(screen, (57, 41, 109), 183, 207.5, -157.8)

def repeteable_slides2(self,screen, text_name):
    zakladka(screen)
    line = self.font.render("Zagrożenia", True, (232, 226, 226))
    screen.blit(line, (36,30.5))
    draw_hex(screen, (57 ,41, 109), 57.1, 824.2, 41)
    split_text(screen, self.font_40, (0,0,0), text_name, 48.3, 70.8, 288)

def last_slides(self, screen, text_name):
    zakladka(screen)
    line = self.font.render("Źródła", True, (232, 226, 226))
    screen.blit(line, (36, 30.5))
    split_text(screen, self.font_small, (0,0,0), text_name,39.1,34.5, 268.6)
    line = self.font_mid.render("Zdjęcia", True, (0,0,0))
    screen.blit(line, (34.5, 205.6))

def transition_slides(self, screen, text_name):
    draw_hex(screen, (83, 67, 137), 119.5, 165.1, -118.6)
    draw_hex(screen, (106, 99, 178), 109.6, 138.9, 44.7)
    draw_hex(screen, (57, 41, 109), 172.95, -124.1, -71.8)
    draw_hex(screen, (83, 67, 137), 115.55, 23.6, 104.5)
    draw_hex(screen, (83, 67, 137), 93.3, 860, -55.8)
    draw_hex(screen, (106, 99, 178), 119.75, 969.4, -26.1)
    draw_hex(screen, (57, 41, 109), 172.95, 1116.2, -71.8)
    draw_hex(screen, (83, 67, 137), 115.55, 1126.3, 104.5)
    draw_hex(screen, (83, 67, 137), 93.1, 1220.4, 490.7)
    draw_hex(screen, (57, 41, 109), 172.95, 1089.9, 608.9)
    draw_hex(screen, (112, 115, 189), 127.95, 1006.8, 476.3)
    draw_hex(screen, (83, 67, 137), 115.5, 932.9, 647)
    draw_hex(screen, (83, 67, 137), 143.51, -84, 479.3)
    draw_hex(screen, (57, 41, 109), 140.45, -33.4, 568.3)
    draw_hex(screen, (83, 67, 137), 132, 139.1, 568.6)
    draw_hex(screen, (112, 115, 189), 109.35, 23.6, 441.2)
    split_text(screen, self.font, (0, 0, 0,), text_name, 93.8, 330.1, 277.3)


class slide_change:
    def __init__(self):
        self.font = pygame.font.SysFont("Times New Roman", 62, True)
        self.font_mid = pygame.font.SysFont("Times New Roman", 30, True)
        self.font_small = pygame.font.SysFont("Times New Roman", 24)
        self.font_40 = pygame.font.SysFont("Times New Roman", 40, True)
        self.background_color = (232 ,226, 226)

    def slide(self, screen, slide_nr):
        match slide_nr:
            case 0:
                draw_hex(screen, (57, 41, 109), 140.9, 1133, 573.8)
                draw_hex(screen, (57, 41, 109), 115.5, 912.4, 695.6)
                draw_hex(screen, (91, 85, 159), 115.1, 894.3, 469)
                draw_hex(screen, (91, 85, 159), 109.3, 693.7, 357.7)
                draw_hex(screen, (57, 41, 109), 140.9, 647, 573.8)
                draw_hex(screen, (83, 67, 137), 132, 1077.9, 318.7)
                draw_hex(screen, (106, 99, 178), 119.7, 863, 215.8)
                draw_hex(screen, (106, 99, 178), 140.9, 1068.9, 48)
                draw_hex(screen, (112, 115, 189), 81.6, 725.8, 133.7)
                split_text(screen, self.font, (0,0,0), "texts/slajd1.txt", 98.3, 60, 101.7)
                split_text(screen, self.font_small, (0,0,0), "texts/slide1_1.txt", 39.1, 60, 588.7)

            case 1:
                transition_slides(self, screen, "texts/slide2.txt")

            case 2:
                draw_hex(screen, (57 ,41 ,109), 130, 494.7, 0)
                rectangle = pygame.Rect((0,0), (625, 226.5))
                pygame.draw.rect(screen, (57, 41, 109), rectangle)
                split_text(screen, self.font, (232, 226, 226), "texts/slide3_title.txt", 93.8, 19.5, 26.7 )
                split_text(screen, self.font_mid, (0,0,0), "texts/slide3_text.txt", 48.3, 119, 335.7)
                split_text(screen, self.font_mid, (0,0,0), "texts/slide3_text2.txt", 48.3, 738.4, 292.9)
                draw_hex(screen, (83, 67, 137), 83.3, 671.4, -71.6)
                draw_hex(screen, (83, 67, 137), 88.3, 589.8, 139)
                draw_hex(screen, (232, 226, 226), 140.9, -96.7, 646.9)
                draw_hex(screen, (83, 67, 137), 93.5, 1204.6, -54)
                draw_hex(screen, (112, 115, 189), 73, 1075.4, 44.5)
                draw_hex(screen, (112, 115, 189), 59.5, 1238.6, 139.1)
                draw_hex(screen, (112, 115, 189), 140.5, -96.7, 646.9)

            case 3:
                draw_hex(screen, (57, 41, 109), 1013.8/2, -317.1, -32.7)
                line = self.font.render("Sprzęt VR", True, (232, 226, 226))
                screen.blit(line, (30,51.5))
                split_text(screen, self.font_mid,(232, 226, 226),"texts/slide4.txt", 48.3, 30, 197.9)
                transform_image(screen, "photos/rekawice_haptyczne.png", (364.9, 316), (632.2, 27.6))
                transform_image(screen, "photos/bierznia.png", (364.9, 316), (956.5,222))
                transform_image(screen, "photos/vr_gogle.png", (364.9, 316), (632.2, 425.1))

            case 4:
                line = self.font.render("Historia VR",True, (0,0,0))
                screen.blit(line, (469.9,50.8))
                split_text(screen, self.font_mid, (0,0,0), "texts/slide5.txt", 48.3, 16.7, 270.9)
                draw_hex(screen, (57 ,41 ,109), 140.9, -72.5, -63.1)
                draw_hex(screen, (106, 99, 178), 109, 144.8, -102.9)
                draw_hex(screen, (83, 67, 137), 99.7, 79.5, 54.2)
                draw_hex(screen, (112, 115, 189), 63.5, 276, 94.3)
                draw_hex(screen, (106, 99, 178), 119.2, 967.6, -120.8)
                draw_hex(screen, (57 ,41, 109), 140.5, 1166.4, -93.2)
                draw_hex(screen, (83 ,67, 137), 144, 1087, 35)
                draw_hex(screen, (112 ,115, 189), 71, 944, 87)
                transform_image(screen, "photos/stereoskop.png", (452,391.7), (880,282.1))

            case 5:
                line = self.font.render("Historia VR", True, (0,0,0))
                screen.blit(line, (29.5,27.6))
                split_text(screen, self.font_mid, (0,0,0), "texts/slide6.txt", 48.3, 29.5, 182.4)
                draw_hex(screen, (57 ,41 ,109), 255, 935, -110.5)
                draw_hex(screen, (112 ,115, 189), 176, 1038, 484)
                draw_hex(screen, (112 ,115, 189), 176, 636, 484)
                transform_image(screen, "photos/miecz.png", (532, 461), (708, 153))

            case 6:
                transition_slides(self,screen, "texts/slide7.txt")

            case 7:
                repeatable_slides(self,screen,"photos/ikona_edukacja.png", "texts/slide8.txt", "photos/vr_edukacja.png")

            case 8:
                repeatable_slides(self,screen,"photos/ikona_edukacja.png", "texts/slide9.txt", "photos/vr_nauka.png")

            case 9:
                repeatable_slides(self, screen, "photos/ikona_gra.png", "texts/slide10.txt","photos/rozrywka.png")

            case 10:
                repeatable_slides(self, screen, "photos/ikona_gra.png", "texts/slide11.txt","photos/bierzniavr.png" )

            case 11:
                repeatable_slides(self, screen, "photos/ikona_samolot.png", "texts/slide12.txt", "photos/symulatorlotu.png")

            case 12:
                repeatable_slides(self, screen,"photos/ikona_samolot.png", "texts/slide13.txt", "photos/lotvr.png")


            case 13:
                repeatable_slides(self, screen, "photos/ikona_medycyna.png", "texts/slide14.txt", "photos/vr_medycyna.png")

            case 14:
                repeatable_slides(self, screen, "photos/ikona_medycyna.png", "texts/slide15.txt", "photos/vr_operacja.png")

            case 15:
                repeteable_slides2(self,screen, "texts/slide16.txt")
                line  = self.font_mid.render("Uzależnienie", True, (0,0,0))
                line1 = self.font_mid.render("1)", True, (232 ,226 ,226))
                screen.blit(line, (959.4,74.5))
                screen.blit(line1, (873.2,66.5))

            case 16:
                repeteable_slides2(self, screen, "texts/slide17.txt")
                line = self.font_mid.render("Uzależnienie", True, (0, 0, 0))
                line1 = self.font_mid.render("2)", True, (232, 226, 226))
                screen.blit(line, (959.4, 74.5))
                screen.blit(line1, (873.2, 66.5))

            case 17:
                repeteable_slides2(self, screen, "texts/slide18.txt")
                line = self.font_mid.render("Problemy zdrowotne", True, (0, 0, 0))
                line1 = self.font_mid.render("3)", True, (232, 226, 226))
                screen.blit(line, (959.4, 74.5))
                screen.blit(line1, (873.2, 66.5))

            case 18:
                repeteable_slides2(self, screen, "texts/slide19.txt")
                line = self.font_mid.render("Problemy zdrowotne", True, (0, 0, 0))
                line1 = self.font_mid.render("4)", True, (232, 226, 226))
                screen.blit(line, (959.4, 74.5))
                screen.blit(line1, (873.2, 66.5))

            case 19:
                repeteable_slides2(self, screen, "texts/slide20.txt")
                line = self.font_mid.render("Prywatność", True, (0, 0, 0))
                line1 = self.font_mid.render("5)", True, (232, 226, 226))
                screen.blit(line, (959.4, 74.5))
                screen.blit(line1, (873.2, 66.5))

            case 20:
                repeteable_slides2(self, screen, "texts/slide21.txt")
                line = self.font_mid.render("Prywatność", True, (0, 0, 0))
                line1 = self.font_mid.render("6)", True, (232, 226, 226))
                screen.blit(line, (959.4, 74.5))
                screen.blit(line1, (873.2, 66.5))

            case 21:
                draw_hex(screen, (57, 41, 109), 201.45, 453.7, 214.5)
                draw_hex(screen, (57, 41, 109), 201.45, 110.1, 22.5)
                draw_hex(screen, (57, 41, 109), 201.45, 793.3, 15.3)
                draw_hex(screen, (57, 41, 109), 201.45, 110.1, 406.5)
                draw_hex(screen, (57, 41, 109), 201.45, 453.7, 214.5)
                draw_hex(screen, (57, 41, 109), 201.45, 793.2, 399.3)
                line = self.font_40.render("Podsumowanie", True, (232, 226, 226))
                screen.blit(line, (530.7, 361.5))
                split_text(screen, self.font_40,(232, 226, 226), "texts/slide22_LT.txt", 48.3, 168.3, 104.2)
                split_text(screen, self.font_40, (232, 226, 226), "texts/slide22_LB.txt", 48.3, 155.8, 543.2)
                split_text(screen, self.font_40, (232, 226, 226), "texts/slide22_RT.txt", 48.3, 900.1, 104.2)
                split_text(screen, self.font_40, (232, 226, 226), "texts/slide22_RB.txt", 48.3, 838.7, 513.8)

            case 22:
                last_slides(self, screen, "texts/slide23.txt")

            case 23:
                last_slides(self, screen, "texts/slide24.txt")

            case 24:
                sys.exit()








                


                
        