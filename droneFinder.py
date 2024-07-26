import cv2
import argparse
import numpy as np
import os

def find_color_in_frame(frame, lower_color, upper_color):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def process_video(video_path, lower_color, upper_color):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return    
    if not os.path.exists('frames'):
        os.makedirs('frames')
    
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        contours = find_color_in_frame(frame, lower_color, upper_color)
        
        if contours:
            frame_filename = os.path.join('frames', f'frame_{frame_count}.jpg')
            cv2.imwrite(frame_filename, frame)
            #delay eh a quntidade de frames por segundo que sera mostrada, mudando esse valor, voce altera a velocidade de reproducao do video
            delay = 5
        else:
            delay = 5
        
        for contour in contours:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)
        
        cv2.imshow('Frame', frame)
        
        frame_count += 1
        
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analisar frames de um vídeo em busca de uma cor específica.')
    parser.add_argument('video_path', type=str, help='Caminho para o vídeo a ser processado')
    args = parser.parse_args()

    #Aqui que se define os parametros para a procura das cores, voce pode pesquisar no google os valores que 
    #se assemelha as helices do seu drone ou usar esse color picker feito pelo Renato <3 
    # https://github.com/RenatoBrittoAraujo/color-picker-opencv.git
    
    # Esta configurado para os valotes HSV de rosa meio vibrante, cor das helices do meu finado drone
    lower_color = np.array([140, 100, 100]) 
    upper_color = np.array([170, 255, 255])
    
    process_video(args.video_path, lower_color, upper_color)

