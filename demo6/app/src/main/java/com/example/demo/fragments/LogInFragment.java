package com.example.demo.fragments;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

import com.example.demo.R;
import com.example.demo.TruyenDN;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link LogInFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class LogInFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";
    EditText name,pass;
    Button dangnhap;
    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;
    TruyenDN truyenDN;



    public LogInFragment() {
        // Required empty public constructor

    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment LogInFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static LogInFragment newInstance(String param1, String param2) {
        LogInFragment fragment = new LogInFragment();
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
        truyenDN = (TruyenDN) getActivity();
        View rootView = inflater.inflate(R.layout.fragment_log_in, container, false);
        final EditText tenDangNhap = (EditText) rootView.findViewById(R.id.editTextEmailDN);
        final EditText matKhau = (EditText) rootView.findViewById(R.id.editTextMatKhauDN);
        Button dangnhap=(Button)rootView.findViewById(R.id.buttonDangNhap);

        dangnhap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String tenText = tenDangNhap.getText().toString().trim();
                String pass=matKhau.getText().toString().trim();
                //Toast.makeText(getActivity(),tenText+"    "+pass,Toast.LENGTH_LONG).show();
                truyenDN.DataDN(tenText,pass);

            }
        });

        return rootView;
    }




}