package com.example.demo.fragments;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import com.example.demo.CustomAdapter;
import com.example.demo.NewsActivity;
import com.example.demo.R;
import com.example.demo.ReadNews;
import com.example.demo.XMLDOMParser;

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

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link ScienceFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class ScienceFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;
    ListView lvHome;
    TextView txtTitle;
    ImageView imageViewLogo;

    CustomAdapter customAdapter;
    ArrayList<ReadNews> arrayReadNews;
    public ScienceFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment ScienceFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static ScienceFragment newInstance(String param1, String param2) {
        ScienceFragment fragment = new ScienceFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_home, container, false);

        lvHome = (ListView) view.findViewById(R.id.listViewHome);
        txtTitle = (TextView) view.findViewById(R.id.textViewHome);
        imageViewLogo = (ImageView) view.findViewById(R.id.imageViewLogo);

        txtTitle.setText("Khoa Học");
        imageViewLogo.setImageResource(R.drawable.ic_menu_science);

        arrayReadNews = new ArrayList<ReadNews>();

        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                new ReadData().execute("https://vnexpress.net/rss/khoa-hoc.rss");

            }
        });

        return view;
    }

    class ReadData extends AsyncTask<String ,Integer, String>
    {

        @Override
        protected String doInBackground(String... strings) {
            return docNoiDung_Tu_URL(strings[0]);
        }

        @Override
        protected void onPostExecute(String s) {
            XMLDOMParser parser = new XMLDOMParser();
            Document document = parser.getDocument(s);
            NodeList nodeList = document.getElementsByTagName("item");
            NodeList nodeListDescriptoin = document.getElementsByTagName("description");
            String hinhAnh = "";
            String title = "";
            String link = "";
            String des = "";
            for(int i = 0;i < nodeList.getLength();i++)
            {
                String cdata = nodeListDescriptoin.item(i+1).getTextContent();
                Pattern p = Pattern.compile("<img[^>]+src\\s*=\\s*['\"]([^'\"]+)['\"][^>]*>");
                Matcher matcher = p.matcher(cdata);
                if(matcher.find()){
                    hinhAnh = matcher.group(1);
                }

                Element element = (Element) nodeList.item(i);
                title = parser.getValue(element,"title");
                link = parser.getValue(element,"link");
                p = Pattern.compile("</a></br>.*");
                matcher = p.matcher(cdata);
                if (matcher.find())
                {
                    des = matcher.group(0);
                    des = des.replaceAll("</a></br>","");
                }
                arrayReadNews.add(new ReadNews(title,link,hinhAnh,des));
            }
            customAdapter = new CustomAdapter(getActivity(),android.R.layout.simple_list_item_1,arrayReadNews);
            lvHome.setAdapter(customAdapter);
            lvHome.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                    Intent intent = new Intent(getActivity(), NewsActivity.class);
                    intent.putExtra("LinkTinTuc",arrayReadNews.get(position).getLink());
                    startActivity(intent);
                }
            });
            super.onPostExecute(s);
        }
    }

    private String docNoiDung_Tu_URL(String theUrl){
        StringBuilder content = new StringBuilder();
        try    {
            URL url = new URL(theUrl);
            URLConnection urlConnection = url.openConnection();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
            String line;
            while ((line = bufferedReader.readLine()) != null){
                content.append(line + "\n");
            }
            bufferedReader.close();
        }
        catch(Exception e)    {
            e.printStackTrace();
        }
        return content.toString();
    }
}