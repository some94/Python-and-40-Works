import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400
# pygame 초기화
pygame.init()
clock = pygame.time.Clock()
# 스크린 설정. 600 x 400 픽셀로 설정.
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():    # pygame 이벤트 가져오기
            if event.type == pygame.QUIT:   # [X] 버튼을 누르면 종료
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    # 키 다운 입력 중에 스페이스 바가 눌리면 space 출력
                if event.key == pygame.K_SPACE:
                    print("space")
                    
        clock.tick(FPS)     # FPS 설정. 1초에 몇 프레임이 동작할지 결정.(60FPS로 동작)
        screen.fill((255, 255, 255))    # 화면을 흰색으로 채움
        
        pygame.display.update() # 화면을 그림

if __name__ == '__main__':
    main()