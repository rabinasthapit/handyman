package tcpProgrammingMultithread;

import java.io.IOException;
import java.io.DataInputStream;
import java.io.DataOutputStream;

import java.net.Socket;

import java.util.Scanner;

public class ClientTcp {
	public static void main(String[] args) {
		try {
		Socket s=new Socket("localhost",3432);
		DataInputStream dis=new DataInputStream(s.getInputStream());
		DataOutputStream dos=new DataOutputStream(s.getOutputStream());
		Scanner sc=new Scanner(System.in);
		System.out.println("Type message: bye to quit");
		boolean flag=true;
		String str="";
		while(flag) {
			str=sc.nextLine();
			if(str.equalsIgnoreCase("bye")){
				flag=false;
			}
			else {
				dos.writeUTF(str);
				System.out.println("Server:"+dis.readUTF());
			}
		}
		sc.close();
		s.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
