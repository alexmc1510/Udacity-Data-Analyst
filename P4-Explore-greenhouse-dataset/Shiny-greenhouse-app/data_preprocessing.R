library(tidyverse)
library(WDI)

# Read the geojson dataset for choropleth
# From http://data.okfn.org/data/core/geo-countries#data
countries <- geojsonio::geojson_read("data/countries.geojson", what = "sp")

# Topologically-aware geometry simplification using rmapshaper package, 
# keep = proportion of points to retain
countries_simple <- rmapshaper::ms_simplify(countries, keep = 0.05, keep_shapes = TRUE)
save(countries_simple, file = "data/countries_simple.RData")

# Download the greenhouse gas emissions data for year 1970 - 2012 
# by using the World Bank's API,parse the resulting JSON file, 
# and format it in the long country-year format.

wb_ghg <- WDI(country = "all",
indicator = "EN.ATM.GHGT.KT.CE",
start = 1970,
end = 2012,
extra = TRUE) %>% 
  filter(!is.na(region)) %>% 
  filter(!(region == "Aggregates")) %>% 
  select(EN.ATM.GHGT.KT.CE, iso3c, year, country)

# Saving on object in RData format for loading the data in Shiny app
save(wb_ghg, file = "data/wb_ghg.RData")
