#pragma once
#include"Enigma.h"
#include<unordered_map>
#include<iostream>

//Konstruktor********************************************
Enigma::Enigma(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	this->walze1 = walze1;
	this->walze2 = walze2;
	this->walze3 = walze3;

	this->stellung1 = stellung1;
	this->stellung2 = stellung2;
	this->stellung3 = stellung3;

	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}


//Getter*************************************************
int Enigma::get_walze1() { return walze1; }
int Enigma::get_walze2() { return walze2; }
int Enigma::get_walze3() { return walze3; }

int Enigma::get_stellung1() { return stellung1; }
int Enigma::get_stellung2() { return stellung2; }
int Enigma::get_stellung3() { return stellung3; }

std::unordered_map<char, char> Enigma::get_Steck() { return Steck; }


//Setter*************************************************
void Enigma::set_walze1(int w1) { walze1 = w1; }
void Enigma::set_walze2(int w2) { walze2 = w2; }
void Enigma::set_walze3(int w3) { walze3 = w3; }

void Enigma::set_stellung1(int s1) { stellung1 = s1; }
void Enigma::set_stellung2(int s2) { stellung2 = s2; }
void Enigma::set_stellung3(int s3) { stellung3 = s3; }

void Enigma::set_Steck(std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}


//Funktionen*********************************************

//Funktion zum ‰ndern der Einstellungen nachdem die Enigma-Klasse erstellt wurde
void Enigma::einstellungen(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10) {
	this->walze1 = walze1;
	this->walze2 = walze2;
	this->walze3 = walze3;

	this->stellung1 = stellung1;
	this->stellung2 = stellung2;
	this->stellung3 = stellung3;

	Steck = { {steck1[0],steck1[1]},{steck2[0],steck2[1]},{steck3[0],steck3[1]},{steck4[0],steck4[1]},{steck5[0],steck5[1]},{steck6[0],steck6[1]},{steck7[0],steck7[1]},{steck8[0],steck8[1]},{steck9[0],steck9[1]},{steck10[0],steck10[1]} };
}

/*
//Funktion die die Eingabe von der Konsole einlieﬂt und aufbereitet zum kodieren
std::string Enigma::prepare_input() {

}
*/

//Funkion die einen string aufbereitet zum kodieren
std::string Enigma::prepare_Input(std::string input) {
	std::string output = "";
	for (int i = 0; i < input.size(); i++) {
		if (char(input[i]))
			//ASCII BULLSHIT
	}
}

//Funktion die den kodierungsmechanismus umsetzt
std::string Enigma::encrypt(std::string input) {

}