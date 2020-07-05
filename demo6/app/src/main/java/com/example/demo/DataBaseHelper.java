package com.example.demo;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.widget.Toast;

import androidx.annotation.Nullable;

public class DataBaseHelper extends SQLiteOpenHelper{


    public DataBaseHelper(@Nullable Context context) {
        super(context, "login.db", null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("Create table user(email text primary key, ten text, password text)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("drop table if exists user");
    }

    public  boolean insert(String email,String ten,String password)
    {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put("email",email);
        contentValues.put("ten",ten);
        contentValues.put("password",password);
        long inc = db.insert("user",null,contentValues);
        if(inc == -1) return false;
        else return  true;
    }

    public boolean checkEmail(String email)
    {
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("Select * from user where email=?",new String[]{email});
        if(cursor.getCount()>0) return false;
        else return true;

    }

    public boolean checkEmailPassword(String email,String password)
    {
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("select * from user where email=? and password=?",new String[]{email,password});
        if(cursor.getCount()>0) return false;
        else return true;
    }

    public User getUser(String email) {
        SQLiteDatabase db = this.getReadableDatabase();

        Cursor cursor = db.rawQuery("Select * from user where email=?",new String[]{email});

        if(cursor.getCount() == 0) return null;
        else
        {
            User user;
            String emailUser = "";
            String tenUser = "";
            String passwordUser = "";

            while (cursor.moveToNext())
            {
                emailUser = cursor.getString(0);
                tenUser = cursor.getString(1);
                passwordUser = cursor.getString(2);
            }
            user = new User(tenUser,emailUser,passwordUser);
            return user;
        }
    }
}
