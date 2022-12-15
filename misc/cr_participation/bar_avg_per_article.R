install.packages("ggplot")
install.packages("dplyr")
library(ggplot2)
library(dplyr)
setwd("yourwd")
part_bd <- read.csv("part_bd.csv")

#Get mean of part_bd
art_mean_by_format <- part_bd %>%
  group_by(shortname, format) %>%
  summarise_at(vars(part_num), list(mean = mean))
art_mean_by_format

#Get mean of part_bd
art_mean <- part_bd %>%
  group_by(shortname) %>%
  summarise_at(vars(part_num), list(mean = mean))
art_mean

#Plot mean of part_bd
ggplot() +
  geom_bar(data=art_mean_by_format, 
           aes(x=shortname, 
               y=mean, 
               fill=format),
           stat="identity",
           position = "dodge",
           width = 0.7,
           alpha=0.9)+
  geom_label(data=art_mean,
            aes(x=shortname, 
                y=mean, 
                label=round(mean, digits=2)),
            alpha=0.6,
            fontface="bold",
            label.size=0.1)+
  theme_bw()+
  xlab("Class Number")+
  ylab("Average Number of Contributions")+
  labs(title = "Article Discussion Popularity", 
       subtitle="Average contributions per class for each article, grouped by format",
       caption = "Data Source: Personal UIC2101 Grade Records")
