//use later to put video
//[![Video Title](http://img.youtube.com/vi/VIDEO_ID/0.jpg)](http://www.youtube.com/watch?v=VIDEO_ID "Video Title")


//ramesh ask me to teach below c code in my youtube.
//But I am not going to make a video.
//Because I am lazy.

#include <stdio.h>

void increment_a(int a) {
    a++;
    printf("0.This is a: %d\n", a);
}

void increment_b(int *b){
    (*b)++;
    printf("0.This is b: %d\n", *b);
}


int main(void) {
    int     a = 5;
    int     b = 10;

    increment_a(a);
    increment_b(&b);

    printf("1.This is a: %d\n", a);
    printf("1.This is b: %d\n", b);
}
