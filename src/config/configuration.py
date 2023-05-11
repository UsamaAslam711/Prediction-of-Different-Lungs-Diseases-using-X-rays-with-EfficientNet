from ensure import ensure_annotations
from src.entity.config_entity import *
from src.constant import *
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.utils.utils import read_yaml_file

class Configuration:
    
    
    def __init__(self, config_file_path = CONFIG_FILE_PATH,
                 current_time_stamp = CURRENT_TIME_STAMP) -> None :
        
        self.config_file_info = read_yaml_file(file_path = config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        """
        Returns a named tuple containg file paths of all directories required for data ingestion.
        
            Parameters: None

            Returns: 
                data_ingestion_config (named tuple) -> It contains file path for the following directiories
                
                    1. Ziped_Data (Contains downloaded ziped data)
                    2. Raw_Data (Contains raw train, test and val data)
                    3. Ingested_CSV_Data (Contains csv train,test and val data)
                    4. Train_CSV_Data (Contains train csv data)
                    5. Test_CSV_Data (Contains test csv data)
                    6. Val_CSV_Data (Contains val csv data)
        """
        
        try:
            
            # Path to artifact directory
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            
            # Path to data_ingestion in artifcat directory
            data_ingestion_artifcat_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            data_ingestion_config_file_info = self.config_file_info[DATA_INGESTION_CONFIG_KEY]
            
            
            # Contains source to data
            data_source_url = data_ingestion_config_file_info[DATA_INGESTION_DOWNLOAD_URL]
            
            # Path to ziped_data in data_ingestion//artifact
            local_zip_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_ZIP_DATA_DIR]
            )
            
            
            # Path to raw_data in data_ingestion//artifact
            local_raw_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_RAW_DATA_DIR]
            )
            
            
            # Path to ingested_csv_data in data_ingestion//artifact
            local_ingested_csv_data_dir = os.path.join(
                data_ingestion_artifcat_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_INGESTED_CSV_DATA_DIR]
            )
            
            # Path to train_csv_data in ingested_csv_data//data_ingestion//artifact
            local_train_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_TRAIN_CSV_DATA_DIR]
            )
            
            # Path to test_csv_data in ingested_csv_data//data_ingestion//artifact
            local_test_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_TEST_CSV_DATA_DIR]
            )
            
            # Path to val_csv_data in ingested_csv_data//data_ingestion//artifact
            local_val_csv_data_dir = os.path.join(
                local_ingested_csv_data_dir,
                data_ingestion_config_file_info[DATA_INGESTION_LOCAL_VAL_CSV_DATA_DIR]
            )
            
            
            data_ingestion_config = DataIngestionConfig(
                data_source_url=data_source_url,
                local_zip_data_dir= local_zip_data_dir,
                local_raw_data_dir = local_raw_data_dir,
                local_ingested_csv_data_dir = local_ingested_csv_data_dir,
                local_train_csv_data_dir = local_train_csv_data_dir,
                local_test_csv_data_dir = local_test_csv_data_dir,
                local_val_csv_data_dir = local_val_csv_data_dir
            )
            
            logging.info(f" Data Ingestion Config : [{data_ingestion_config}]")
            
            return data_ingestion_config
            
            
        except Exception as e:
            raise CustomException(sys,e) from e
        
        
    def get_data_validation_config(self) -> DataValidationConfig:
        
        """
        Returns a named tuple containg file paths of all directories required for data validation.
        
        Parameters: None

        Returns: 
            data_validation_config (named tuple) -> It contains file path for the following directiories
                
                1. Schema_File_Path (Path to schema.yml file in config dir)
                2. Train_Data_Validation_File_Path (Path to a directory having all train data validation reports)
                3. Test_Data_Validation_File_Path (Path to a directory having all test data validation reports)
                4. Val_Data_Validation_File_Path (Path to a directory having all val data validation reports)
        """
        try:
            
            # Path to artifact directory
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            # Path to data validation in artifact directory
            data_validation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATION_ARTIFACT_DIR,
                CURRENT_TIME_STAMP
            )
            
            data_validation_config_file_info = self.config_file_info[DATA_VALIDATION_CONFIG_KEY]
            
            # Path to schema file in config dir
            schema_file_path = os.path.join(
                ROOT_DIR,
                data_validation_config_file_info[DATA_VALIDATION_SCHEMA_DIR_NAME],
                data_validation_config_file_info[DATA_VALIDATION_SCHEMA_FILE_NAME]
            )
            
            # Path to data validation reports dir 
            data_validation_reports = os.path.join(
                data_validation_artifact_dir,
                data_validation_config_file_info[DATA_VALIDATION_REPORTS]
            )
            
            data_validation_config = DataValidationConfig(
                schema_file_path=schema_file_path,
                data_validation_reports_file_path=data_validation_reports,
            )
            
            return data_validation_config
            
            
        except Exception as e:
            raise CustomException(sys,e) from e
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        """
        Returns a named tuple containg file paths of all directories required for data transformation.
        
        Parameters: None

        Returns: 
            data_transformation_config (named tuple) -> It contains file path for the following directiories
                
                1. Transformed_Train_Data_Dir (Path to a directory having transformed train iamges)
                2. Transformed_Test_Data_Dir (Path to a directory having transformed test images)
                3. Transformed_Val_Data_Dir (Path to a directory having transformed validation images)
        """
        
        try:
            
            # Path to artifact directory
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            # Path to data transformation in artifact directory
            data_transformation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_DIR,
                CURRENT_TIME_STAMP
            )
            
            data_transformation_config_file_info = self.config_file_info[DATA_TRANSFORMATION_CONFIG_KEY]
            
            # Path to transformed_data in data_transformation//artifact
            transformed_data_dir = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_config_file_info[DATA_TRANSFORMATION_DIR_NAME]
            )
            
            # Path to train in transformed_data//data_transformation//artifact
            transformed_train_data_dir = os.path.join(
                transformed_data_dir,
                data_transformation_config_file_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME]
            )
            
            # Path to test in transformed_data//data_transformation//artifact
            transformed_test_data_dir = os.path.join(
                transformed_data_dir,
                data_transformation_config_file_info[DATA_TRANSFORMATION_TEST_DIR_NAME]
            )
            
            # Path to val in transformed_data//data_transformation//artifact
            transformed_val_data_dir = os.path.join(
                transformed_data_dir,
                data_transformation_config_file_info[DATA_TRANSFORMATION_VAL_DIR_NAME]
            )
            
            data_transformation_config = DataTransformationConfig(
                transformed_train_data_dir = transformed_train_data_dir,
                transformed_test_data_dir = transformed_test_data_dir,
                transformed_val_data_dir = transformed_val_data_dir
            )
            
            return data_transformation_config
            
        except Exception as e:
            raise CustomException(sys,e) from e
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        
        """
        Returns a named tuple containg path to artifact directory.
        
            Parameters: None

            Returns:
                training_pipeline_config (named tuple): Contains complete path of artifact directory.
        """
        
        
        try:
            training_pipeline_config = self.config_file_info[TRAINING_PIPELINE_CONFIG_KEY] 
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR]) 
            
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            
            logging.info(f" Training Pipeline Config : [{training_pipeline_config}]")
            
            
            return training_pipeline_config
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        

