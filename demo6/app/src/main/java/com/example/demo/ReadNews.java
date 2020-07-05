package com.example.demo;

public class ReadNews {
    private String title;
    private String link;
    private String image;
    private String des;

    public String getTitle() {
        return title;
    }

    public String getLink() {
        return link;
    }

    public String getImage() {
        return image;
    }

    public String getDes() { return des;
    }

    public ReadNews(String title, String link, String image, String des) {
        this.title = title;
        this.link = link;
        this.image = image;
        this.des = des;
    }
}
