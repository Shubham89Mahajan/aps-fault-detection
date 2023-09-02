from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from sensor.components import data_ingestion

def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_Exception")
          result = 3/0
          print(result)
          logging.info("Stoping the test_logger_and_Exception")
     except Exception as e:
          logging.debug(str(e))
          raise SensorException(e, sys)


if __name__=="__main__":
     try:
          #get_collection_as_dataframe(database_name="aps", collection_name="sensor")
          training_pipeline_config = TrainingPipelineConfig()
          data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          raise SensorException(e, sys)