library(shinydashboard)
library(tidyverse)
library(ggvis)
library(leaflet)
library(WDI)
library(sp)
library(rgdal)


# Read the dataset for Lineplots
ghg_complete <- read_csv("data/wb_ghg_complete.csv",
                         col_types = cols(
                           IncomeGroup = col_factor(
                             levels = c("High income", 
                                        "Upper middle income",
                                        "Lower middle income",
                                        "Low income")),
                           Region = col_factor(
                             levels = c("East Asia & Pacific",
                                        "Europe & Central Asia",
                                        "North America",
                                        "Latin America & Caribbean",
                                        "Sub-Saharan Africa",
                                        "South Asia",
                                        "Middle East & North Africa")
                           )
                         ))