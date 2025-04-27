
#define SAMPLE_RATE 500 //500hz
#define NUM_SAMPLES 5000 
#define ANALOG_PIN 15 
#define INTERNAL_LED 2 

uint16_t buffer[NUM_SAMPLES];

void setup() {
  // 11 dB: 0V to ~3.3V
  // 12 bit resolution 0-4095
  analogSetAttenuation(ADC_11db);
  
  Serial.begin(115200);
  pinMode(ANALOG_PIN, INPUT);
  pinMode(ANALOG_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) 
  {
    char command = Serial.read(); // Read the command from the computer
    if (command == 's') 
    { 
      clearBuffer();
      startRecording();
      sendDataToComputer();
    }
  }
}

void startRecording() {

  unsigned long sampleInterval = 1000000 / SAMPLE_RATE; // In Microseconds
  unsigned long startTime = micros();
  for (int i = 0; i < NUM_SAMPLES; i++) {
    while (micros() - startTime < sampleInterval); // Wait for next sample
    buffer[i] = analogRead(ANALOG_PIN); // Read analog value
    startTime += sampleInterval;
  }
}

void sendDataToComputer() {
  for (int i = 0; i < NUM_SAMPLES; i++) {
    Serial.println(buffer[i]);
  }
  Serial.println("DONE"); // End of transmission
}

void clearBuffer() {
    for (int i = 0; i < NUM_SAMPLES; i++) {
        buffer[i] = 0;  // Reset each element to 0
    }
}
