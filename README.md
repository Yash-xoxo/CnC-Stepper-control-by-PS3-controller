# Stepper Motor Control with PS3 Joystick

This project allows controlling **two stepper motors** using a **PS2 controller's analog sticks**. The left joystick controls one motor, and the right joystick controls the other. When you move a joystick, the corresponding motor moves; when you release it, the motor stops.

## Features
- **Real-time movement:** Motors respond immediately when the joystick is moved.
- **Simultaneous control:** Both motors can move at the same time.
- **Adjustable speed:** Easily change the stepper motor speed by modifying delay values.
- **Serial communication:** Commands are sent via the serial monitor or external controller.

## Hardware Requirements
- Arduino (Uno, Mega, etc.)
- PS2 Controller
- Stepper motors (2x)
- Stepper motor drivers (A4988, DRV8825, or similar)
- Power supply (appropriate for the motors)
- Jumper wires

## Wiring Diagram
| Arduino Pin | Connection |
|------------|------------|
| **2**  | Step pin for Motor X |
| **5**  | Direction pin for Motor X |
| **3**  | Step pin for Motor Y |
| **6**  | Direction pin for Motor Y |
| **8**  | Enable pin |

## Installation & Usage
1. **Connect the hardware** as per the wiring diagram.
2. **Upload the Arduino sketch** (provided in `stepper_control.ino`) to your Arduino board.
3. **Open the Serial Monitor** (baud rate: `9600`).
4. **Send commands** using the joystick:
   - Move left joystick **forward/backward** → Motor X moves **forward/backward**
   - Move right joystick **forward/backward** → Motor Y moves **forward/backward**
   - Release joystick → The motor stops

## Serial Commands (For Testing)
If using a serial monitor, you can control the motors using these keys:
```
X  -> Move Motor X Forward
x  -> Move Motor X Backward
Y  -> Move Motor Y Forward
y  -> Move Motor Y Backward
S  -> Stop Both Motors
```

## Adjusting Speed
Modify the `delay()` values in `loop()` to change motor speed. **Increasing the delay slows down the motor**:
```cpp
// Change delay to control speed
#define STEP_DELAY 5 // Adjust this value
```

## License
This project is open-source under the **MIT License**. Feel free to modify and use it!

## Contributing
Pull requests are welcome! If you find issues or want improvements, submit an issue or PR.

---

### 📌 **Author:** Yash

