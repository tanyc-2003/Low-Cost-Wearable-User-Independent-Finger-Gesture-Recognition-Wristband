#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
#include "EMGFilters.h"

#define SAMPLE_RATE 500 //500hz
#define NUM_SAMPLES 250

#define SensorInputPin1 36 // 36 39 34
#define SensorInputPin2 39 // 36 39 34
#define SensorInputPin3 34 // 36 39 34

uint16_t buffer1[NUM_SAMPLES];
uint16_t buffer2[NUM_SAMPLES];
uint16_t buffer3[NUM_SAMPLES];
uint16_t buffer_chained[NUM_SAMPLES * 3];


static int Throhold = 0;
EMGFilters myFilter;

void setup() {
  // 11 dB: 0V to ~3.3V
  // 12 bit resolution 0-4095
  analogSetAttenuation(ADC_11db);

  Serial.begin(115200);

  myFilter.init(SAMPLE_FREQ_500HZ, NOTCH_FREQ_50HZ, true, true, true);

}

void loop() {

  if (Serial.available() > 0) 
  {
    char command = Serial.read(); // Read the command from the computer
    if (command == 'a') 
    {
      clearBuffer();
      startRecording();
      chain(buffer1, buffer2, buffer3, buffer_chained);
      sendDataToComputer(buffer_chained);
    }
  }

}

void startRecording() {

  unsigned long sampleInterval = 1000000 / SAMPLE_RATE; // In Microseconds
  unsigned long startTime = micros();
  for (int i = 0; i < NUM_SAMPLES; i++) {
    while (micros() - startTime < sampleInterval); // Wait for next sample

    // Read ADC1 channels
    int val1 = analogRead(SensorInputPin1);  // Read GPIO36
    int val2 = analogRead(SensorInputPin2);  // Read GPIO39
    int val3 = analogRead(SensorInputPin3);  // Read GPIO34

    buffer1[i] =  filter(val1);
    buffer2[i] =  filter(val2);
    buffer3[i] =  filter(val3);

    startTime += sampleInterval;
  }

  Serial.println("DONE"); // Done recoridng

}

int filter(int Value) {
  // filter processing
  int DataAfterFilter = myFilter.update(Value / 4);
  int envlope = sq(DataAfterFilter);
  envlope = (envlope > Throhold) ? envlope : 0; // any value under throhold will be set to zero

  return envlope;
}

void chain(uint16_t buff1[], uint16_t buff2[], uint16_t buff3[], uint16_t buffOut[]) {
  // Copy buff1 to buffOut
  for (int i = 0; i < NUM_SAMPLES; i++) {
    buffOut[i] = buff1[i];
  }

  // Copy buff2 to buffOut after buff1
  for (int i = 0; i < NUM_SAMPLES; i++) {
    buffOut[NUM_SAMPLES + i] = buff2[i];
  }

  // Copy buff3 to buffOut after buff2
  for (int i = 0; i < NUM_SAMPLES; i++) {
    buffOut[2 * NUM_SAMPLES + i] = buff3[i];
  }
}

void sendDataToComputer(uint16_t buff[]) {
  Serial.write((uint8_t*)buff, NUM_SAMPLES * 3 * sizeof(uint16_t)); // Send raw binary data
}


void clearBuffer() {
  for (int i = 0; i < NUM_SAMPLES; i++) {
    buffer1[i] = 0;  // Reset each element to 0
    buffer2[i] = 0;
    buffer3[i] = 0;
  }
  for (int i = 0; i < NUM_SAMPLES * 3; i++) {
//    Serial.println(buffer_chained[i]);
    buffer_chained[i] = 0;
  }
}
