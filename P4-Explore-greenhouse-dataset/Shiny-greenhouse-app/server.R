# Load the simplified geojson data for countries
load("data/countries_simple.RData")

# Load the greenhouse gas emissions data for year 1970 - 2012 
load("data/wb_ghg.RData")

function(input, output, session) {
  
  # Interactive Choropleth map.........................................................
  
  # Reactive expression for the data subsetted to what the user selected
  countries_plus_ghg <- reactive({
    
    # Filter the data to select for the year user selected
    wb_ghg_subset <- filter(wb_ghg, year == input$year)
    
    # Merge a Spatial object having a data.frame for Choropleth map
    sp::merge(countries_simple, wb_ghg_subset, 
              by.x = "ISO_A3", by.y = "iso3c")
  })
  
  # Create the map
  output$choropleth_ghg <- renderLeaflet({
    leaflet(countries_simple) %>% 
      setView(0, 20, zoom = 1) %>%
      addTiles()
  })
  
  # Observer to change the color of countries, labels and legends
  # based on the year user selects in the UI
  observe({
    dat <- countries_plus_ghg()
    
    # Define numeric vector bins to add some color
    bins <- ggplot2:::breaks(c(min(dat$EN.ATM.GHGT.KT.CE, na.rm = TRUE)
                               ,max(dat$EN.ATM.GHGT.KT.CE, na.rm = TRUE)),
                             "width",n = 5)
    
    # Call colorBin to generate a palette function that maps the RColorBrewer 
    #"YlOrRd" colors to our bins.
    pal <- colorBin("YlGnBu", 
                    domain = dat$EN.ATM.GHGT.KT.CE, 
                    bins =  bins)
    
    # Generate the labels with some HTML
    labels <- sprintf(
      "<strong>%s</strong><br/>%g",
      dat$country, dat$EN.ATM.GHGT.KT.CE
    ) %>% lapply(htmltools::HTML)
    
    leafletProxy("choropleth_ghg", data = dat) %>% 
      addPolygons(
        fillColor = ~pal(EN.ATM.GHGT.KT.CE),
        weight = 1,
        opacity = 1,
        color = "white",
        fillOpacity = 0.7,
        highlight = highlightOptions(
          weight = 2,
          color = "#666",
          dashArray = "",
          fillOpacity = 0.7,
          bringToFront = TRUE),
        label = labels,
        labelOptions = labelOptions(
          style = list("font-weight" = "normal", padding = "3px 8px"),
          textsize = "15px",
          direction = "auto")) %>% 
      clearControls() %>% 
      addLegend(pal = pal, values = ~EN.ATM.GHGT.KT.CE, opacity = 0.7, 
                title = "Emissions (kt of CO2 equivalent)",
                position = "bottomleft")
  })
  
  # Lineplot.............................................................................
  
  # Country select input box for Line plot
  ghg_subset_p1 <- reactive({
    ghg_complete %>% 
      filter(Country %in% c(input$country))
  })
  
  # Function for the tooltip
  all_values <- function(x) {
    if(is.null(x)) return(NULL)
    paste0("<b>", format(x), "<b>", collapse = "<br>")
  }
  
  # Reactive expression with the ggvis plot
  # Create GHG emission per year by country- lineplot
  p1 <- reactive({
      ghg_subset_p1 %>% 
      ggvis(~Year, ~Emissions, stroke= ~Country) %>% 
      layer_points(size = 1, fill = ~Country, fillOpacity := 0.2,
                   size.hover := 100, fillOpacity.hover := 0.5) %>% 
      layer_lines() %>% 
      add_axis("x", values = seq(1970, 2012, by = 5)) %>% 
      add_axis("y", title_offset = 75) %>% 
      add_tooltip(all_values, "hover") %>% 
      set_options(renderer="canvas", width = "auto", height = "auto")
  })
  
  p1 %>% bind_shiny("ghg_by_country")
  
  
  # Barplot..................................................................................
  
  # Combine the selected variables into a new data frame
  ghg_subset_p2 <- reactive({
    ghg_complete %>% 
      filter(!Country == "World") %>% 
      filter(Year == input$year2) %>% 
      arrange(desc(Emissions)) %>% 
      do(head(.,input$n))
  })
  
  output$top_emitters <- renderPlot({
    p2 <- ggplot(ghg_subset_p2(),
                 aes(x = reorder(Country, Emissions), 
                     y = Emissions)) +
      geom_bar(stat = "identity") +
      labs(x = "Country",
           y = "Emissions (kt of CO2 equivalent)") +
      coord_flip() +
      theme_bw() +
      theme(axis.text.x=element_text(vjust = 0.5))
    print(p2)
  })
}