package com.example.demo;

public class User {

    private String hoTen;
    private String email;
    private String matKhau;


    public String getHoTen() {
        return hoTen;
    }

    public String getEmail() {
        return email;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setMatKhau(String matKhau) {
        this.matKhau = matKhau;
    }

    public String getMatKhau() {
        return matKhau;
    }

    public User(String hoTen, String email, String matKhau) {
        this.hoTen = hoTen;
        this.email = email;
        this.matKhau = matKhau;
    }
}
