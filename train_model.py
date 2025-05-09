import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Now import and run the trainer
from FinBot import trainer

if __name__ == "__main__":
    print("Starting model training...")
    
    # Train the intent model
    print("Training intent model...")
    trainer.train_intent_model()
    
    # Train the dialog model
    print("Training dialog model...")
    trainer.train_dialog_model()
    
    print("Training completed successfully!") 