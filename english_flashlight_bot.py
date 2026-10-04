from plyer import flash
import time

print("--- 🤖 YOUR PYTHON LIGHT ROBOT IS READY ---")
print("=" * 60)
print("👉 JUST TYPE: light")
print("-" * 50)

try:
    # ১. ইনপুট লজিক: ইউজারের কাছ থেকে সহজ ইংলিশ কমান্ড নেওয়া
    user_command = input("✍️ Enter your command here: ").strip().lower()
    print("=" * 60)
    
    # 🎯 ২. আসল ইংলিশ লজিক: তুমি 'light' লিখলে লাইট অন হবে
    if user_command == "light":
        print("💡 Order Accepted! Turning on the Flashlight...")
        flash.on() # লাইট অন করা হলো
        
        print("⏱️ Waiting for 5 seconds...")
        time.sleep(5) # ৫ সেকেন্ড লাইটটি জ্বলে থাকবে
        
        flash.off() # লাইট অফ করা হলো
        print("🔌 5 seconds over! Light turned off automatically.")
        
    else:
        print("❌ Wrong Command! Spelling mistake.")
        print("👉 You must type exactly: light")

except Exception as e:
    print(f"🛑 System Error: {e}")

print("=" * 60)
print("--- 💸 Robot Session Finished Successfully! ---")
