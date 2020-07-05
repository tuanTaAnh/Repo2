package com.example.demo;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.sqlite.SQLiteDatabase;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.demo.fragments.BusinessFragment;
import com.example.demo.fragments.CultureFragment;
import com.example.demo.fragments.EnvironmentFragment;
import com.example.demo.fragments.FashionFragment;
import com.example.demo.fragments.HomeFragment;
import com.example.demo.fragments.LogInFragment;
import com.example.demo.fragments.ScienceFragment;
import com.example.demo.fragments.SignUpFragment;
import com.example.demo.fragments.SocietyFragment;
import com.example.demo.fragments.SportFragment;
import com.example.demo.fragments.WorldFragment;
import com.google.android.material.navigation.NavigationView;
import com.google.gson.Gson;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener, TruyenDK, TruyenDN {

    private DrawerLayout drawerLayout;
    NavigationView navigationView;
    DataBaseHelper db;
    TextView userName;
    User user;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        drawerLayout = findViewById(R.id.drawerLayout);
        if (user == null){
            user = getUser();
        }
        db = new DataBaseHelper(this);


        ImageView imageView = findViewById(R.id.imageMenu);

        imageView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                drawerLayout.openDrawer(GravityCompat.START);
            }
        });

        navigationView = findViewById(R.id.navigationView);

        navigationView.setNavigationItemSelectedListener(this);


        navigationView.setItemIconTintList(null);

        View headerView = navigationView.getHeaderView(0);

        userName = (TextView) headerView.findViewById(R.id.username);

        if(user != null)
        {
            userName.setText(user.getHoTen());
        }

        if(savedInstanceState == null)
        {
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                    new HomeFragment()).commit();

            navigationView.setCheckedItem(R.id.menuHome);
        }

    }


    @Override
    public void onBackPressed() {
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }


    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {

        switch (item.getItemId())
        {
            case R.id.menuHome:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new HomeFragment()).commit();
                break;
            case R.id.menuWorld:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new WorldFragment()).commit();
                break;
            case R.id.menuScience:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new ScienceFragment()).commit();
                break;
            case R.id.menuSport:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new SportFragment()).commit();
                break;
            case R.id.menuEnvironment:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new EnvironmentFragment()).commit();
                break;
            case R.id.menuSociety:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new SocietyFragment()).commit();
                break;
            case R.id.menuFashion:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new FashionFragment()).commit();
                break;
            case R.id.menuBusiness:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new BusinessFragment()).commit();
                break;
            case R.id.menuCulture:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new CultureFragment()).commit();
                break;
            case R.id.menulogIn:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new LogInFragment()).commit();
                break;
            case R.id.menuSignUp:
                getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                        new SignUpFragment()).commit();
                break;
        }

        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }


    @Override
    public void DataDK(String email,String ten, String matkhau) {
        Boolean checkEmail = db.checkEmail(email);
        if(checkEmail==true)
        {
            Boolean insert = db.insert(email,ten,matkhau);
            Toast.makeText(MainActivity.this,"email: "+email,Toast.LENGTH_LONG).show();
//            Toast.makeText(MainActivity.this,ten,Toast.LENGTH_LONG).show();
//            Toast.makeText(MainActivity.this,matkhau,Toast.LENGTH_LONG).show();
//            Toast.makeText(MainActivity.this,"Đăng Ký Thành Công",Toast.LENGTH_LONG).show();
            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                    new HomeFragment()).commit();
            navigationView.setCheckedItem(R.id.menuHome);
        }
        else
        {
            Toast.makeText(MainActivity.this,"Email Đã Tồn Tại",Toast.LENGTH_LONG).show();
        }
    }


    @Override
    public void DataDN(String email, String matkhau) {
        Boolean checkemailpass = db.checkEmailPassword(email,matkhau);
        if(checkemailpass!=true)
        {
            Toast.makeText(MainActivity.this,"Đăng Nhập Thành Công",Toast.LENGTH_LONG).show();
            user = db.getUser(email);

            userName.setText(user.getHoTen());

            getSupportFragmentManager().beginTransaction().replace(R.id.fragment_container,
                    new HomeFragment()).commit();
            save();
            navigationView.setCheckedItem(R.id.menuHome);
        }
        else
        {
            Toast.makeText(MainActivity.this,"Đăng Nhập Thất Bại",Toast.LENGTH_LONG).show();
        }

    }


    @Override
    // Initialize the contents of the Activity's options menu
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the Options Menu we specified in XML
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    // This method is called whenever an item in the options menu is selected.
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            Toast.makeText(MainActivity.this,"Settings",Toast.LENGTH_LONG).show();
//            Intent settingsIntent = new Intent(this, SettingsActivity.class);
//            startActivity(settingsIntent);
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
    public void save(){
        SharedPreferences sharedPref = this.getPreferences(Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPref.edit();
        Gson gson = new Gson();
        String json = gson.toJson(user);
        editor.putString("user", json);
        editor.commit();
    }

    public User getUser(){
        SharedPreferences sharedPref = MainActivity.this.getPreferences(Context.MODE_PRIVATE);
        Gson gson = new Gson();
        String json = sharedPref.getString("user", null);
        User u = gson.fromJson(json, User.class);
        return u;
    }

}

