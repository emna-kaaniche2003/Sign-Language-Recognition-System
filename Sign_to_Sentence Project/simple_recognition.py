import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# 1. Charger le modèle de reconnaissance (MLP)
# Ce fichier est le "cerveau" qui reconnaît la forme de la main
model = tf.keras.models.load_model("asl_mediapipe_mlp_model.h5")  #

# 2. Configurer la détection (MediaPipe)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# 3. Liste des lettres (Labels)
# L'ordre respecte exactement celui de votre entraînement
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'del', 'nothing', 'space']

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # Effet miroir et détection de la main
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)  # Étape de DÉTECTION

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extraction des points de la main
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            # Étape de RECONNAISSANCE
            # On demande au modèle quelle est cette lettre à cet instant précis
            prediction = model.predict(np.array([landmarks]), verbose=0)
            class_id = np.argmax(prediction)
            lettre = labels[class_id]

            # Étape d'AFFICHAGE (Simple texte sur la vidéo)
            if lettre != "nothing":
                cv2.putText(frame, lettre, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

            # Dessiner le squelette de la main pour voir la détection
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Afficher la fenêtre
    cv2.imshow("Reconnaissance de Lettre", frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()