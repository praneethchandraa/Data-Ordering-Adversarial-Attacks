### TODO

- <del> Setup baseline code and train reference models </del>

ResNet-18 trained on cifar-10 

              precision    recall  f1-score   support

       plane       0.93      0.93      0.93      1000
         car       0.95      0.98      0.96      1000
        bird       0.93      0.88      0.90      1000
         cat       0.86      0.85      0.85      1000
        deer       0.92      0.94      0.93      1000
         dog       0.88      0.88      0.88      1000
        frog       0.93      0.96      0.94      1000
       horse       0.95      0.95      0.95      1000
        ship       0.98      0.94      0.96      1000
       truck       0.95      0.96      0.95      1000

    accuracy                           0.93     10000
    macro avg      0.93      0.93      0.93     10000
    weighted avg   0.93      0.93      0.93     10000



- Implement BRRR attacks and get comparable results

- <del> Batch Reorder </del>
        
              precision    recall  f1-score   support

       plane       0.90      0.89      0.89      1000
         car       0.97      0.92      0.94      1000
        bird       0.73      0.83      0.78      1000
         cat       0.75      0.75      0.75      1000
        deer       0.87      0.84      0.86      1000
         dog       0.80      0.80      0.80      1000
        frog       0.95      0.89      0.92      1000
       horse       0.92      0.92      0.92      1000
        ship       0.92      0.93      0.92      1000
       truck       0.92      0.93      0.93      1000

      accuracy                        0.87     10000
      macro avg    0.87      0.87     0.87     10000
      weighted avg 0.87      0.87     0.87     10000
      
   
- Batch Reshuffle
        
              precision    recall  f1-score   support

       plane       0.78      0.87      0.82      1000
         car       0.88      0.94      0.91      1000
        bird       0.73      0.82      0.77      1000
         cat       0.82      0.53      0.64      1000
        deer       0.76      0.90      0.82      1000
         dog       0.72      0.78      0.75      1000
        frog       0.86      0.89      0.87      1000
       horse       0.89      0.87      0.88      1000
        ship       0.95      0.85      0.90      1000
       truck       0.96      0.82      0.88      1000

      accuracy                         0.83     10000
      macro avg    0.83      0.83      0.83     10000
      weighted avg 0.83      0.83      0.83     10000
    

- Test Attacks on new models (VISION transformes, Capsules??)
- Prepare Report and Presenatation
- Inhect attack code to installations if possible
