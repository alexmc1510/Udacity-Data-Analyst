header <- dashboardHeader(
  title = "Greenhouse gas (GHG) emissions"
  )

## Sidebar content
sidebar <- dashboardSidebar(
  sidebarMenu(
    menuItem("Interactive Choropleth", tabName = "choropleth", icon = icon("map-o")),
    menuItem("Interactive Lineplot", tabName = "lineplot", icon = icon("line-chart")),
    menuItem("Interactive Barplot", tabName = "barplot", icon = icon("bar-chart"))
  )
)  

## Body content
body <- dashboardBody(
  tabItems(
    
    # First tab content
    tabItem("choropleth",
            
      fluidRow(
        column(width = 9,
          box(width = NULL, solidHeader = TRUE,
              title = "Greenhouse gas emissions (kt of CO2 equivalent)",
              leafletOutput("choropleth_ghg", height = 500)
          )
        ),
        column(width = 3,
          box(width = NULL, status = "warning",
            selectInput("year", "Year", 
                          choices = seq(1970, 2012, 1), 
                          selected = 2012)
          )
        )
      )
    ),
    
    # Second tab content
    tabItem("lineplot",
            
      fluidRow(
        column(width = 9,
          box(
            width = NULL, status = "info", solidHeader = TRUE,
            title = "Greenhouse gas emissions (kt of CO2 equivalent)",
            ggvisOutput("ghg_by_country")
          )
        ),
        column(width = 3,
          box(
            width = NULL, status = "info",
            title = "Country",
            selectInput("country", label = NULL,
                        choices = unique(ghg_complete$Country),
                        selected = "World",
                        multiple = TRUE),
            p(
              class = "text-muted",
              paste("Explore this interactive graph:",
                    "You can compare emissions for multiple countries.",
                    "Click on the box for the country names to appear.",
                    "Also, you can hover on the points for more information."
              )
            )
          )
        )
      )
    ),
    
    # Third tab content
    tabItem("barplot",
            
            fluidRow(
              column(width = 9,
                box(
                  width = NULL, status = "info", solidHeader = TRUE,
                  title = "Top greenhouse gas emitters",
                  plotOutput("top_emitters")
                )
              ),
              column(width = 3,
                box(
                  width = NULL, status = "info", 
                  sliderInput("n", label = "Top N emitters",
                              min = 1, max = 50, step = 1,
                              value = 10
                  ),
                  sliderInput("year2", label = "Year", 
                              min = 1970, max = 2012, step = 1,
                              value = 2012, animate = TRUE
                  )
                )
              )
            )
      
    )
  )
)

dashboardPage(
  header,
  sidebar,
  body
)