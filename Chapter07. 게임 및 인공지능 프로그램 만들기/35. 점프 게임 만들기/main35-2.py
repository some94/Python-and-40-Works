import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
# 플레이어 클래스 생성
class Player():
    def __init__(self, x, y):       # 객체를 생성할 떄 초기화
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self):     # 파란색의 네모를 40x40 사이즈로 그림. 반환 값은 좌표와 크기
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def jump(self):     # 플레이어의 점프 구현
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

player = Player(50, MAX_HEIGHT - 40)    # 플레이어 객체를 생성하고 x=50, y는 바닥으로 붙임

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:     # space키를 입력받으면 jump 변수를 참으로 설정
                    player.isJump = True
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        player_rect = player.draw()     # 플레이어를 그린다. 반환 값은 좌표와 크기
        player.jump()   # 점프를 구현. player.isJump가 True이어야 동작.
        
        print(player_rect)
        
        pygame.display.update()

if __name__ == '__main__':
    main()