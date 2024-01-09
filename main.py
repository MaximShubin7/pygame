import sys
import pygame

# Инициация Pygame
pygame.init()

# Установка размеров окна, цветов и загрузка фоновой картинки
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Formula 1')
background_image = pygame.image.load('fon.png')  # Путь к вашему изображению


def map():
    new_screen3 = pygame.display.set_mode((1920, 1080))
    fonmap_image = pygame.image.load('fonmap.png')
    fonmap_image = pygame.transform.scale(fonmap_image, (1920, 1080))

    map_image = pygame.image.load('map.png')  # Загрузка изображения карты
    map_image = pygame.transform.scale(map_image, (800, 600))  # Изменение размеров изображения карты

    # Функция для отображения кнопок и уровня сложности
    def draw_buttons():
        pygame.draw.rect(screen, (0, 255, 0), (50, 250, 50, 50))  # Кнопка для смены картинки влево
        pygame.draw.rect(screen, (0, 255, 0), (900, 250, 50, 50))  # Кнопка для смены картинки вправо

        font = pygame.font.Font(None, 36)
        text = font.render('Уровень сложности: 5', True, (255, 255, 255))
        screen.blit(text, (400, 550))

        pygame.draw.rect(screen, (0, 0, 255), (300, 500, 50, 50))  # Кнопка "Уровень сложности -"
        pygame.draw.rect(screen, (0, 0, 255), (650, 500, 50, 50))  # Кнопка "Уровень сложности +"

    # Функция для отображения изображений
    def draw_images():
        screen.blit(fonmap_image, (0, 0))
        screen.blit(map_image, (550, 100))  # Отображение изображения карты
        draw_buttons()  # Отображение кнопок и уровня сложности

    # Основной цикл программы
    running4 = True
    while running4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 < mouse_x < 100 and 250 < mouse_y < 300:
                    # Действие при нажатии на кнопку смены картинки влево
                    pass  # Добавьте нужное действие здесь
                elif 900 < mouse_x < 950 and 250 < mouse_y < 300:
                    # Действие при нажатии на кнопку смены картинки вправо
                    pass  # Добавьте нужное действие здесь
                elif 300 < mouse_x < 350 and 500 < mouse_y < 550:
                    # Действие при нажатии на кнопку "Уровень сложности -"
                    pass  # Добавьте нужное действие здесь
                elif 650 < mouse_x < 700 and 500 < mouse_y < 550:
                    # Действие при нажатии на кнопку "Уровень сложности +"
                    pass  # Добавьте нужное действие здесь

        screen.fill((0, 0, 0))  # Очистка экрана
        draw_images()  # Отображение изображений и кнопок

        pygame.display.update()
# Функции для действий при нажатии на кнопки
def play_action():
    new_screen = pygame.display.set_mode((1920, 1080))
    map_image = pygame.image.load('map.png')
    map_image = pygame.transform.scale(map_image, (1920, 1080))

    car1_image = pygame.image.load('car1-0.png').convert_alpha()  # Загрузка изображения для первого спрайта без фона
    car1_image = pygame.transform.scale(car1_image, (50, 25))  # Изменение размеров первого спрайта
    car2_image = pygame.image.load('car2-0.png').convert_alpha()  # Загрузка изображения для второго спрайта без фона
    car2_image = pygame.transform.scale(car2_image, (50, 25))  # Изменение размеров второго спрайта

    car1_x = 400  # Начальные координаты первого спрайта
    car1_y = 840
    car2_x = 400  # Начальные координаты второго спрайта
    car2_y = 900

    car1_speed = 10  # Скорость перемещения первого спрайта
    car2_speed = 3  # Скорость перемещения второго спрайта

    # Основной цикл программы
    running2 = True
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        # Управление первым спрайтом с помощью клавиш WASD
        if keys[pygame.K_a]:
            car1_x -= car1_speed
            car1_image = pygame.image.load('car1-180.png').convert_alpha()
            car1_image = pygame.transform.scale(car1_image, (50, 25))
            screen.blit(car1_image, (car1_x, car1_y))
        if keys[pygame.K_d]:
            car1_x += car1_speed
            car1_image = pygame.image.load('car1-0.png').convert_alpha()
            car1_image = pygame.transform.scale(car1_image, (50, 25))
            screen.blit(car1_image, (car1_x, car1_y))
        if keys[pygame.K_w]:
            car1_y -= car1_speed
            car1_image = pygame.image.load('car1-90.png').convert_alpha()
            car1_image = pygame.transform.scale(car1_image, (25, 50))
            screen.blit(car1_image, (car1_x, car1_y))
        if keys[pygame.K_s]:
            car1_y += car1_speed
            car1_image = pygame.image.load('car1-270.png').convert_alpha()
            car1_image = pygame.transform.scale(car1_image, (25, 50))
            screen.blit(car1_image, (car1_x, car1_y))

        # Управление вторым спрайтом с помощью стрелок на клавиатуре
        if keys[pygame.K_LEFT]:
            car2_x -= car2_speed
            car2_image = pygame.image.load('car2-180.png').convert_alpha()
            car2_image = pygame.transform.scale(car2_image, (50, 25))
            screen.blit(car2_image, (car2_x, car2_y))
        if keys[pygame.K_RIGHT]:
            car2_x += car2_speed
            car2_image = pygame.image.load('car2-0.png').convert_alpha()
            car2_image = pygame.transform.scale(car2_image, (50, 25))
            screen.blit(car2_image, (car2_x, car2_y))
        if keys[pygame.K_UP]:
            car2_y -= car2_speed
            car2_image = pygame.image.load('car2-90.png').convert_alpha()
            car2_image = pygame.transform.scale(car2_image, (25, 50))
            screen.blit(car2_image, (car2_x, car2_y))
        if keys[pygame.K_DOWN]:
            car2_y += car2_speed
            car2_image = pygame.image.load('car2-270.png').convert_alpha()
            car2_image = pygame.transform.scale(car2_image, (25, 50))
            screen.blit(car2_image, (car2_x, car2_y))

        new_screen.blit(map_image, (0, 0))  # Очистка экрана
        screen.blit(car1_image, (car1_x, car1_y))  # Отображение первого спрайта
        screen.blit(car2_image, (car2_x, car2_y))  # Отображение второго спрайта
        pygame.display.update()


def rules_action():
    new_screen2 = pygame.display.set_mode((1920, 1080))
    background = pygame.image.load("rules.png")
    background = pygame.transform.scale(background, (1920, 1080))

    running3 = True
    while running3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        new_screen2.blit(background, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        draw_text("Закрыть", 100, (255, 0, 0), screen_width // 2, screen_height // 2 + 250)
        if screen_width // 2 - 100 < mouse[0] < screen_width // 2 + 100 and screen_height // 2 + 225 < mouse[1] \
                < screen_height // 2 + 275 and click[0] == 1:
            running3 = False

        draw_text("Правила", 70, (0, 0, 0), screen_width // 2, 250)
        draw_text("Formula 1 - гонки для настоящих мужчин.", 70, (0, 0, 0), 700, 350)
        draw_text("Цель: Первым проехать 3 круга по треку.", 70, (0, 0, 0), 685, 450)
        draw_text("Управление: Первый игрок управляет болидом с помощью", 70, (0, 0, 0), 910,
                  550)
        draw_text("кнопок WASD, а второй - с помощью стрелочек.", 70, (0, 0, 0), 770, 650)

        pygame.display.update()


def quit_action():
    pygame.quit()
    sys.exit()


# Функция для рисования текста на экране
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    draw_text("ГОНКИ", 150, (255, 255, 255), screen_width // 2, 100)

    # Рисуем кнопки без фона очень большими буквами заданными цветами
    draw_text("Играть", 100, (0, 255, 0), screen_width // 2, screen_height // 2 - 100)
    draw_text("Правила", 100, (0, 0, 255), screen_width // 2, screen_height // 2)
    draw_text("Выход", 100, (255, 0, 0), screen_width // 2, screen_height // 2 + 100)

    pygame.display.update()

    # Проверка нажатия кнопок
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if screen_width // 2 - 100 < mouse[0] < screen_width // 2 + 100:
        if screen_height // 2 - 125 < mouse[1] < screen_height // 2 - 75 and click[0] == 1:
            play_action()
        elif screen_height // 2 - 25 < mouse[1] < screen_height // 2 + 25 and click[0] == 1:
            rules_action()
        elif screen_height // 2 + 75 < mouse[1] < screen_height // 2 + 125 and click[0] == 1:
            quit_action()

pygame.quit()
sys.exit()
