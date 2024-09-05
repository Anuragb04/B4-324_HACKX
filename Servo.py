#include <Servo.h>

Servo MED1;
Servo MED2;

// Define control pins
#define CONTROL_PIN_3 3  // Button to dispense Medicine 1
#define CONTROL_PIN_4 4  // Button to dispense Medicine 2

// Function to handle dispensing medicine from compartment 1
void dispenseMedicine1() {
    Serial.println("Dispensing Medicine 1");
    MED1.write(40);  // Rotate servo to dispense
    delay(1000);     // Delay to simulate medicine dispensing time
    MED1.write(90);  // Return servo to default position
}

// Function to handle dispensing medicine from compartment 2
void dispenseMedicine2() {
    Serial.println("Dispensing Medicine 2");
    MED2.write(140); // Rotate servo to dispense
    delay(1000);     // Delay to simulate medicine dispensing time
    MED2.write(90);  // Return servo to default position
}

void setup() {
    Serial.begin(9600);

    // Attach servos to appropriate pins
    MED1.attach(9);
    MED2.attach(10);

    // Initialize servos to default position
    MED1.write(90);
    MED2.write(90);

    // Define control pins as inputs and enable pull-up resistors
    pinMode(CONTROL_PIN_3, INPUT_PULLUP);
    pinMode(CONTROL_PIN_4, INPUT_PULLUP);
}

void loop() {
    // Add a delay to prevent rapid state changes
    delay(100); // Adjust the delay as needed

    // Read the current state of control pins
    int state_3 = digitalRead(CONTROL_PIN_3);
    int state_4 = digitalRead(CONTROL_PIN_4);

    // Check if the button for Medicine 1 (Control Pin 3) is pressed
    if (state_3 == LOW) {
        dispenseMedicine1();  // Dispense Medicine 1 when button is pressed
        delay(1000);          // Delay to avoid multiple presses
    }

    // Check if the button for Medicine 2 (Control Pin 4) is pressed
    if (state_4 == LOW) {
        dispenseMedicine2();  // Dispense Medicine 2 when button is pressed
        delay(1000);          // Delay to avoid multiple presses
    }
}
