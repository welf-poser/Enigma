#pragma once
#include"Enigma.h"
#include<unordered_map>
#include<iostream>

//Konstruktor********************************************
Enigma::Enigma(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, char UKW,std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	this->walze1 = walze1;
	this->walze2 = walze2;
	this->walze3 = walze3;

	this->stellung1 = stellung1;
	this->stellung2 = stellung2;
	this->stellung3 = stellung3;

	this->UKW = UKW;

	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}


//Getter*************************************************
int Enigma::get_walze1() { return walze1; }
int Enigma::get_walze2() { return walze2; }
int Enigma::get_walze3() { return walze3; }

int Enigma::get_stellung1() { return stellung1; }
int Enigma::get_stellung2() { return stellung2; }
int Enigma::get_stellung3() { return stellung3; }

char Enigma::get_UKW() { return UKW; }

std::unordered_map<char, char> Enigma::get_Steck() { return Steck; }


//Setter*************************************************
void Enigma::set_walze1(int w1) { walze1 = w1; }
void Enigma::set_walze2(int w2) { walze2 = w2; }
void Enigma::set_walze3(int w3) { walze3 = w3; }

void Enigma::set_stellung1(int s1) { stellung1 = s1; }
void Enigma::set_stellung2(int s2) { stellung2 = s2; }
void Enigma::set_stellung3(int s3) { stellung3 = s3; }

void Enigma::set_UKW(char UKW) { this->UKW = UKW; };

void Enigma::set_Steck(std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}


//Funktionen*********************************************

//Funktion zum ändern der Einstellungen nachdem die Enigma-Klasse erstellt wurde
void Enigma::einstellungen(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	this->walze1 = walze1;
	this->walze2 = walze2;
	this->walze3 = walze3;

	this->stellung1 = stellung1;
	this->stellung2 = stellung2;
	this->stellung3 = stellung3;

	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}

//Funkion die einen string aufbereitet zum kodieren
std::string Enigma::prepare_input(std::string input) {
	std::string output = "";
	for (int i = 0; i < input.size(); i++) {
		if (char(input[i]) >= 97 && char(input[i]) <= 122)
			output += char(input[i] - 32);
		else if (char(input[i]) >= 65 && char(input[i]) <= 90)
			output += char(input[i]);

		switch (char(input[i])) {
		case '0':
			output += "NULL";
			break;

		case '1':
			output += "EINS";
			break;

		case '2':
			output += "ZWEI";
			break;

		case '3':
			output += "DREI";
			break;

		case '4':
			output += "VIER";
			break;

		case '5':
			output += "FUENF";
			break;

		case '6':
			output += "SECHS";
			break;

		case '7':
			output += "SIEBEN";
			break;

		case '8':
			output += "ACHT";
			break;

		case '9':
			output += "NEUN";
			break;

		case 'ü':
			output += "UE";
			break;

		case 'Ü':
			output += "UE";
			break;

		case 'ö':
			output += "OE";
			break;
		
		case 'Ö':
			output += "OE";
			break;

		case 'ä':
			output += "AE";
			break;

		case 'Ä':
			output += "AE";
			break;
		}
	}
	return output;
}

//Funktion for encoding or decoding a string
std::string Enigma::encrypt(std::string input) {

	//Prepare input: all Uppercase, remove special characters etc.
	std::string in = prepare_input(input);

	//Implementation Steckboard
	for (int i = 0; i < in.size(); i++) {

		if(Steck[in[i]])
			in[i] = Steck[in[i]];
	}

	//UKW and Walze Index from left to right: UKW, Walze 3, Walze 2, Walze 1, Steckboard.
	/*
	Cipher flow
	UKW <- Walze 3 <- Walze 2 <- Walze 1 <- Steckboard <-!!Input starts here!!
				!Mind the notches/turnovers and ringsetting and so on!
	UKW -> Walze 3 -> Walze 2 -> Walze 1 -> Steckboard ->Output
	*/

	//Initialize which Rotors are selected
	const char* rotor1;
	const char* rotor2;
	const char* rotor3;
	const std::unordered_map<char,char> UKW_selected;

	switch (walze1) {
	case 1:
		rotor1 = WalzeNo1;
		break;
	case 2:
		rotor1 = WalzeNo2;
		break;
	case 3:
		rotor1 = WalzeNo3;
		break;
	case 4:
		rotor1 = WalzeNo4;
		break;
	case 5:
		rotor1 = WalzeNo5;
		break;
	}

	switch (walze2) {
	case 1:
		rotor2 = WalzeNo1;
		break;
	case 2:
		rotor2 = WalzeNo2;
		break;
	case 3:
		rotor2 = WalzeNo3;
		break;
	case 4:
		rotor2 = WalzeNo4;
		break;
	case 5:
		rotor2 = WalzeNo5;
		break;
	}

	switch (walze3) {
	case 1:
		rotor3 = WalzeNo1;
		break;
	case 2:
		rotor3 = WalzeNo2;
		break;
	case 3:
		rotor3 = WalzeNo3;
		break;
	case 4:
		rotor3 = WalzeNo4;
		break;
	case 5:
		rotor3 = WalzeNo5;
		break;
	}
	
	switch (UKW) {
	case 'A':
		UKW_selected = &(this->UKW_A);
		break;

	case 'B':
		UKW_selected = UKW_B;
		break;

	case 'C':
		UKW_selected = UKW_C;
		break;
	}


	std::string out = "";
	
	//Output in words of five characters like the actual ciphertext where
	for (int i = 0; i < in.size(); i++) {
		if (i % 5 == 0 && i != 0)
			out += " ";

		out += in[i];
	}

	return out;
}