package com.example.demo.fragments;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.demo.R;
import com.example.demo.TruyenDK;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link SignUpFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class SignUpFragment extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;
    TruyenDK truyenDK;

    public SignUpFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment SignUpFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static SignUpFragment newInstance(String param1, String param2) {
        SignUpFragment fragment = new SignUpFragment();
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
        truyenDK = (TruyenDK) getActivity();
        View rootView = inflater.inflate(R.layout.fragment_sign_up, container, false);
        final EditText tenDangNhap = (EditText) rootView.findViewById(R.id.editTextTenDK);
        final EditText emailDK = (EditText) rootView.findViewById(R.id.editTextEmailDK);
        final EditText matKhau = (EditText) rootView.findViewById(R.id.editTextMatKhauDK);
        Button dangky=(Button)rootView.findViewById(R.id.buttonDangKy);

        dangky.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String tenTxt = tenDangNhap.getText().toString().trim();
                String emailTxt=emailDK.getText().toString().trim();
                String passTxt=matKhau.getText().toString().trim();

                if(tenTxt.equals("")||emailTxt.equals("")||passTxt.equals(""))
                {
                    Toast.makeText(getActivity(),"Đăng Ký Lỗi", Toast.LENGTH_LONG).show();
                }
                else
                {
                    Toast.makeText(getActivity(),tenTxt, Toast.LENGTH_LONG).show();
                    Toast.makeText(getActivity(),emailTxt, Toast.LENGTH_LONG).show();
                    Toast.makeText(getActivity(),passTxt, Toast.LENGTH_LONG).show();
                    truyenDK.DataDK(emailTxt,tenTxt,passTxt);
                }

            }
        });

        return rootView;
    }
}