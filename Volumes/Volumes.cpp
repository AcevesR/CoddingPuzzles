#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define PI 3.141592

float ask_h(), ask_r(), area(float r);
void print(float);

main() {
      int dec, choice;
      float Vci, Vco, r,h, ar;

      do {
	printf("Hello.\n");
      printf("Do you want to calculate the volume of...? \n1) Cylinder \n2) Cone\n");
      scanf("%i", &dec);
      system("cls");
    
      if(dec == 1) {
      r = ask_r();
      h = ask_h();
      ar = area(r);
      Vci = ar * h;
      print(Vci);
      }

      else if(dec == 2){
      r = ask_r();
      h = ask_h();
      ar = area(r);
    	Vco = (ar * h) / 3;
      print(Vco);
	}

      else {
      printf("\nWrong input.\n");
      system("PAUSE");
      system("cls");
      exit(0);
	}      

      printf("\nDo you want to calculate another volume? \n1)Yes \n2)No\n");
      scanf("%i", &choice);
      system("cls");

      }
	while (choice == 1);
      
	system("PAUSE");
      system("cls");
}

float ask_r() {
      float r;     
      printf("Write the value of the radius\n");
      scanf("%f", &r);
      system("cls");
      return r;
}

float ask_h() {
      float h;     
      printf("Write the value of the height\n");
      scanf("%f", &h);
      system("cls");
      return h;
}

float area(float r) {
     float area_calc;
     area_calc = PI * r * r;
     return area_calc;
}

void print (float Vol) {
     printf("The volume of the figure is %f ", Vol, "\n");
}