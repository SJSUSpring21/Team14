# sMPC for privacy preserving face recognition - Approved by professor

Abstract:
Face recognition is a form of biometric recognition technology that uses a person's facial features to identify them. With the rapid advancement of Internet technology, the technology of analyzing images using deep learning convolutional neural networks has seen a lot of progress in recent years. Face detection is rapidly being used in a variety of fields. Significant privacy concerns have emerged as a result of the widespread use of biometrics. The user's face data is collected by the face recognition system for commercial purposes. Face data is normally one-of-a-kind and irreplaceable, and if it is leaked, it would be disastrous for the user's privacy. Using Secure Multi Protocol Authentication, it can perform face recognition by measuring sensitive data from multiple sources. Face data protection can be assured at the same time.

Approach:
Implementation can be divided into two phases. 

1. Extracts the face embedding data phase
Face attribute embeddings are extracted by the client. The face image is first pre-processed using a face recognition model, and then the deep learning model is used to process the face features in order to extract low-dimensional face representations (face embeddings). The client then sends the private data of face embeddings in a secret sharing manner to two remote non-competing servers.

2. Face recognition privacy preserving phase using sMPC.
Two non-competitive servers use cloud computing to train models using joint multifaceted face embedding data. The parameters of the face recognition privacy security model are stored in the form of confidential shared secret text by the two non-competing servers after training. Later, by integrating the face embedding data to be identified, the trained model is used to identify the face.The recognition result is still returned to the client in the form of secret ciphertext. The client decodes the code to obtain the plain text recognition result and completes the face recognition of the user.

Persona: 
Biometrics, Information security, smart cards, surveillance system

Dataset links:
Faces collected from web

Architecture diagram:









