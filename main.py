from src.Pipeline.Stages_of_Pipeline import DataIngestionPipeline
from src.Pipeline.Stages_of_Pipeline import DataValidationPipeline
from src.Pipeline.Stages_of_Pipeline import DataTransformPipeline
from src.Pipeline.Stages_of_Pipeline import ModelTrainPipeline
from src.Pipeline.Stages_of_Pipeline import ModelEvaluationPipeline
                                            #  DataTransformPipeline,ModelTrainPipeline,ModelEvaluationPipeline
                                            
import os 

try:
    print("Enter the Data Ingeston")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    print("-------------------------")
except Exception as e:
    raise e     

try:
    print("Enter the Data validation")
    validation = DataValidationPipeline()
    validation.main()
    print("-------------------------")
except Exception as e:
    raise e  

try:
    print("Enter the Data Transform")
    transform = DataTransformPipeline()
    transform.main()
    print("-------------------------")
except Exception as e:
    raise e  

try:
    print("Enter the model train")
    trainer = ModelTrainPipeline()
    trainer.main()
    print("-------------------------")
except Exception as e:
    raise e  

try:
    print("Enter the model evaluation")
    evaluation = ModelEvaluationPipeline()
    evaluation.main()
    print("-------------------------")
except Exception as e:
    raise e  

