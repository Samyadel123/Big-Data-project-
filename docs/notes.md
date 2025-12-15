## first steps 

- weather conditions and traffic behavior 
#### weather data set 
- Date & time
- City (single city: London)
- Season
- Temperature
- Humidity
- Rainfall
- Wind speed
- Visibility
- Weather condition
- Air pressure

#### traffic dataset 
- Date & time
- City (same city: London)
- Area / district
- Vehicle count
- Average speed
- Accident count
- Congestion level
- Road condition
- Visibility

## Data lake Architecture

1. Genrate Synthetic data 
2. Save the data to Minio as CSV file 
3. Loud the data to cleaning pipeline 
4. Save the cleaned Parquet Data 
5. Copy data to HDFS 
6. Do the monte carlo + Factor analysis 
7. final Gold layer (final results and reports)


# url 
hadoop : http://localhost:9870

minio : http://localhost:9001
