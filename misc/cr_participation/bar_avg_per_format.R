install.packages("ggplot")
install.packages("dplyr")
library(ggplot2)
library(dplyr)
setwd("yourwd")
part_bd <- read.csv("part_bd.csv")

#Get mean for teaching format
format_mean <- part_bd %>%
  group_by(format) %>%
  summarise_at(vars(part_num), list(mean = mean, sd=sd))
format_mean

meanl <- "Mean:"
stdl <- "SD:"

#plot mean for teaching format
ggplot(data=format_mean, aes(x=format, y=mean, fill=format)) +
  geom_bar(stat="identity",
           alpha=0.9,
           width=0.5)+
  #label mean and SD on bar
  geom_text(aes(label=paste(meanl,
                            round(mean, digits=2),
                            "\n",
                            stdl,
                            round(sd, digits=2))),
            nudge_y=-4, 
            fontface="bold",
            size=5,
            color="white")+
  theme_bw()+
  ylim(0,10)+
  theme(legend.position="none")+
  xlab("Class Format")+
  ylab("Average Number of Contributions")+
  labs(title = "Average Class Participation by Format", 
       subtitle="Average number of contributions per class for each learning format",
       caption = "Data Source: Personal UIC2101 Grade Records")
