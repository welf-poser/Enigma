#pragma once
#include"Enigma.h"
#include<unordered_map>
#include<iostream>

class Enigma {
private:

	//Walzen zur Auswahl -> 3 davon werden ausgew�ht
	//Notch Q (17)
	char const WalzeNo1[26] = { 'E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J' };
	
	//Notch E (5)
	char const WalzeNo2[26] = { 'A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E' };
	
	//Notch V (22)
	char const WalzeNo3[26] = { 'B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O' };
	
	//Notch J (10)
	char const WalzeNo4[26] = { 'E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B' };
	
	//Notch Z (26)
	char const WalzeNo5[26] = { 'V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K' };
	
	//Notch Z und M, (26) und (13)
	char const WalzeNo6[26] = { 'J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W' };
	char const WalzeNo7[26] = { 'N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T' };
	char const WalzeNo8[26] = { 'F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V' };

	//Umkehrwalzen
	std::unordered_map<char, char> const UKW_A = { {'A','E'},{'B','J'},{'C','M'},{'D','Z'},{'F','L'},{'G','Y'},{'H','X'},{'I','V'},{'K','W'},{'N','R'},{'O','Q'},{'P','U'},{'S','T'} };
	std::unordered_map<char, char> const UKW_B = { {'A','Y'},{'B','R'},{'C','U'},{'D','H'},{'E','Q'},{'F','S'},{'G','L'},{'I','P'},{'J','X'},{'K','N'},{'M','O'},{'T','Z'},{'V','W'} };
	std::unordered_map<char, char> const UKW_C = { {'A','F'},{'B','V'},{'C','P'},{'D','J'},{'E','I'},{'G','O'},{'H','Y'},{'K','R'},{'L','Z'},{'M','X'},{'N','W'},{'Q','T'},{'S','U'} };


	//Einstellungen**********************************************************************

	//Walzenstellung
	int walze1;
	int walze2;
	int walze3;

	//Ringstellung
	int stellung1;
	int stellung2;
	int stellung3;

	//Steckverbindungen
	std::unordered_map<char, char> Steck;


public:
	
	//Konstruktor********************************************
	Enigma(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10);


	//Getter*************************************************
	int get_walze1();
	int get_walze2();
	int get_walze3();

	int get_stellung1();
	int get_stellung2();
	int get_stellung3();

	std::unordered_map<char, char> get_Steck();


	//Setter*************************************************
	void set_walze1(int w1);
	void set_walze2(int w2);
	void set_walze3(int w3);

	void set_stellung1(int s1);
	void set_stellung2(int s2);
	void set_stellung3(int s3);

	void set_Steck(std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10);


	//Funktionen*********************************************
	
	//Funktion zum �ndern der Einstellungen nachdem die Enigma-Klasse erstellt wurde
	void einstellungen(int walze1, int walze2, int walze3, int stellung1, int stellung2, int stellung3, std::string steck1, std::string steck2, std::string steck3, std::string steck4, std::string steck5, std::string steck6, std::string steck7, std::string steck8, std::string steck9, std::string steck10);
	
	/*
	//Funktion die die Eingabe von der Konsole einlie�t und aufbereitet zum kodieren
	std::string prepare_input();
	*/

	//Funkion die einen string aufbereitet zum kodieren
	std::string prepare_Input(std::string input);

	//Funktion die den kodierungsmechanismus umsetzt
	std::string encrypt(std::string input);
};