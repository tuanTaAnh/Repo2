package com.example.demo;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.List;

public class CustomAdapter extends ArrayAdapter<ReadNews> {

    public CustomAdapter(Context context, int resource, List<ReadNews> items) {
        super(context, resource, items);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        View view = convertView;
        if (view == null) {
            LayoutInflater inflater = LayoutInflater.from(getContext());
            view =  inflater.inflate(R.layout.line_news_layout, null);
        }
        ReadNews p = getItem(position);
        if (p != null) {
            // Anh xa + Gan gia tri
            TextView txtTitle = (TextView) view.findViewById(R.id.textViewTitle);
            TextView txtDes = view.findViewById(R.id.textViewDescription);
            txtDes.setText(p.getDes());
            txtTitle.setText(p.getTitle());

            ImageView imageView = (ImageView) view.findViewById(R.id.imageViewNews);
            Picasso.with(getContext()).load(p.getImage()).into(imageView);
        }
        return view;
    }

}
