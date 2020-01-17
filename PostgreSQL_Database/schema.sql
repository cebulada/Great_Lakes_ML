-- This is for a table for a list of means which will
-- be used to create default values for the website
CREATE TABLE lake_means (
  lake VARCHAR(255) NOT NULL,
  conductivity DOUBLE PRECISION,
  hardness DOUBLE PRECISION,
  turbidity DOUBLE PRECISION,
  chlorophyll DOUBLE PRECISION,
  ammonia DOUBLE PRECISION,
  nitrate_ite DOUBLE PRECISION,
  aluminum DOUBLE PRECISION,
  barium DOUBLE PRECISION,
  calcium DOUBLE PRECISION,
  carbon DOUBLE PRECISION,
  chloride DOUBLE PRECISION,
  chromium DOUBLE PRECISION,
  copper DOUBLE PRECISION,
  magnesium DOUBLE PRECISION,
  manganese DOUBLE PRECISION,
  mercury DOUBLE PRECISION,
  molybdenum DOUBLE PRECISION,
  phosphorus DOUBLE PRECISION,
  potassium DOUBLE PRECISION,
  silicon DOUBLE PRECISION,
  sodium DOUBLE PRECISION,
  strontium DOUBLE PRECISION,
  sulphate DOUBLE PRECISION,
  vanadium DOUBLE PRECISION,
  zinc DOUBLE PRECISION
);

-- This is a master list of all metadata and data
CREATE TABLE master_data (
  lake VARCHAR(255) NOT NULL,
  water_body VARCHAR(255),
  date_collect DATE, -- this should be in the format yyyy-mm-dd
  station_num DOUBLE PRECISION,
  sample_num VARCHAR(255),
  station_descr VARCHAR(1023),
  latitude VARCHAR(255),
  longitude VARCHAR(255),
  conductivity DOUBLE PRECISION,
  hardness DOUBLE PRECISION,
  turbidity DOUBLE PRECISION,
  chlorophyll DOUBLE PRECISION,
  ammonia DOUBLE PRECISION,
  nitrate_ite DOUBLE PRECISION,
  aluminum DOUBLE PRECISION,
  barium DOUBLE PRECISION,
  calcium DOUBLE PRECISION,
  carbon DOUBLE PRECISION,
  chloride DOUBLE PRECISION,
  chromium DOUBLE PRECISION,
  copper DOUBLE PRECISION,
  magnesium DOUBLE PRECISION,
  manganese DOUBLE PRECISION,
  mercury DOUBLE PRECISION,
  molybdenum DOUBLE PRECISION,
  phosphorus DOUBLE PRECISION,
  potassium DOUBLE PRECISION,
  silicon DOUBLE PRECISION,
  sodium DOUBLE PRECISION,
  strontium DOUBLE PRECISION,
  sulphate DOUBLE PRECISION,
  vanadium DOUBLE PRECISION,
  zinc DOUBLE PRECISION
);


-- This is a master list of all metadata
CREATE TABLE metadata (
  lake VARCHAR(255) NOT NULL,
  water_body VARCHAR(255),
  date_collect DATE, -- this should be in the format yyyy-mm-dd
  station_num DOUBLE PRECISION,
  sample_num VARCHAR(255),
  station_descr VARCHAR(1023),
  latitude VARCHAR(255),
  longitude VARCHAR(255)
);


-- This is a master list of all data
CREATE TABLE data (
  lake VARCHAR(255) NOT NULL,
  conductivity DOUBLE PRECISION,
  hardness DOUBLE PRECISION,
  turbidity DOUBLE PRECISION,
  chlorophyll DOUBLE PRECISION,
  ammonia DOUBLE PRECISION,
  nitrate_ite DOUBLE PRECISION,
  aluminum DOUBLE PRECISION,
  barium DOUBLE PRECISION,
  calcium DOUBLE PRECISION,
  carbon DOUBLE PRECISION,
  chloride DOUBLE PRECISION,
  chromium DOUBLE PRECISION,
  copper DOUBLE PRECISION,
  magnesium DOUBLE PRECISION,
  manganese DOUBLE PRECISION,
  mercury DOUBLE PRECISION,
  molybdenum DOUBLE PRECISION,
  phosphorus DOUBLE PRECISION,
  potassium DOUBLE PRECISION,
  silicon DOUBLE PRECISION,
  sodium DOUBLE PRECISION,
  strontium DOUBLE PRECISION,
  sulphate DOUBLE PRECISION,
  vanadium DOUBLE PRECISION,
  zinc DOUBLE PRECISION
);


-- Get what the numbers indicate for great lake labels
-- ex. 0 is "erie"
CREATE TABLE encoded_lakes (
  lake VARCHAR(255) NOT NULL,
  lake_encode INT
);


-- Training Dataset
CREATE TABLE train_lakes (
  lake INT NOT NULL,
  conductivity DOUBLE PRECISION,
  hardness DOUBLE PRECISION,
  turbidity DOUBLE PRECISION,
  chlorophyll DOUBLE PRECISION,
  ammonia DOUBLE PRECISION,
  nitrate_ite DOUBLE PRECISION,
  aluminum DOUBLE PRECISION,
  barium DOUBLE PRECISION,
  calcium DOUBLE PRECISION,
  carbon DOUBLE PRECISION,
  chloride DOUBLE PRECISION,
  chromium DOUBLE PRECISION,
  copper DOUBLE PRECISION,
  magnesium DOUBLE PRECISION,
  manganese DOUBLE PRECISION,
  mercury DOUBLE PRECISION,
  molybdenum DOUBLE PRECISION,
  phosphorus DOUBLE PRECISION,
  potassium DOUBLE PRECISION,
  silicon DOUBLE PRECISION,
  sodium DOUBLE PRECISION,
  strontium DOUBLE PRECISION,
  sulphate DOUBLE PRECISION,
  vanadium DOUBLE PRECISION,
  zinc DOUBLE PRECISION
);


-- Testing Dataset
CREATE TABLE test_lakes (
  lake INT NOT NULL,
  conductivity DOUBLE PRECISION,
  hardness DOUBLE PRECISION,
  turbidity DOUBLE PRECISION,
  chlorophyll DOUBLE PRECISION,
  ammonia DOUBLE PRECISION,
  nitrate_ite DOUBLE PRECISION,
  aluminum DOUBLE PRECISION,
  barium DOUBLE PRECISION,
  calcium DOUBLE PRECISION,
  carbon DOUBLE PRECISION,
  chloride DOUBLE PRECISION,
  chromium DOUBLE PRECISION,
  copper DOUBLE PRECISION,
  magnesium DOUBLE PRECISION,
  manganese DOUBLE PRECISION,
  mercury DOUBLE PRECISION,
  molybdenum DOUBLE PRECISION,
  phosphorus DOUBLE PRECISION,
  potassium DOUBLE PRECISION,
  silicon DOUBLE PRECISION,
  sodium DOUBLE PRECISION,
  strontium DOUBLE PRECISION,
  sulphate DOUBLE PRECISION,
  vanadium DOUBLE PRECISION,
  zinc DOUBLE PRECISION
);
