import streamlit as st
import random

# Define a list of fun facts in English and their Urdu translations
fun_facts = [
    ('Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.', 
     'کیا آپ جانتے ہیں کہ شہد کبھی باسی نہیں ہوتا؟ ماہرین آثار قدیمہ نے قدیم مصری مقبروں میں 3,000 سال پرانے شہد کے برتن پائے ہیں جو ابھی بھی کھانے کے قابل ہیں۔'),
    ('A group of flamingos is called a "flamboyance."', 
     'فلیمنگوز کے گروپ کو "فلیموئنس" کہا جاتا ہے۔'),
    ('Octopuses have three hearts and blue blood.', 
     'آکٹوپس کے تین دل اور نیلا خون ہوتا ہے۔'),
    ('Bananas are berries, but strawberries are not.', 
     'کیلے بیری ہوتے ہیں، لیکن اسٹرابیری نہیں۔'),
    ('An adult human body is made up of about 60% water.', 
     'ایک بالغ انسان کا جسم تقریباً 60% پانی پر مشتمل ہوتا ہے۔'),
    ('A day on Venus is longer than a year on Venus.', 
     'زہرہ پر ایک دن زہرہ کے ایک سال سے لمبا ہے۔'),
    ('Humans share 60% of their DNA with bananas.', 
     'انسانوں کا 60% ڈی این اے کیلے کے ساتھ مشترک ہوتا ہے۔'),
    ('The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.', 
     'ایفل ٹاور گرمیوں میں تھرمل توسیع کی وجہ سے 15 سینٹی میٹر لمبا ہو سکتا ہے۔'),
    ('A cow-bison hybrid is called a "beefalo."', 
     'گائے اور بائسن کا ہائبرڈ "بیفالو" کہلاتا ہے۔'),
    ('The longest word in the English language is "pneumonoultramicroscopicsilicovolcanoconiosis."', 
     'انگریزی زبان کا سب سے لمبا لفظ "پنیومونولٹرامائیکروسکوپکسلیکاوولکینوکونیووسس" ہے۔'),
    ('Slugs have four noses.', 
     'سلاگ کے چار ناک ہوتے ہیں۔'),
    ('A newborn kangaroo is the size of a lima bean.', 
     'نیا پیدا ہونے والا کینگرو لیمہ پھلی کے برابر ہوتا ہے۔'),
    ('There are more stars in the universe than grains of sand on all the Earth’s beaches.', 
     'کائنات میں زمین کے تمام ساحلوں پر موجود ریت کے دانوں سے زیادہ ستارے ہیں۔'),
    ('A group of owls is called a "parliament."', 
     'اولز کے گروپ کو "پارلیمنٹ" کہا جاتا ہے۔'),
    ('Sharks have been around longer than trees.', 
     'شارکس درختوں سے زیادہ عرصے سے موجود ہیں۔'),
    ('A jiffy is an actual unit of time: 1/100th of a second.', 
     'جِفِی وقت کی ایک حقیقی اکائی ہے: 1/100 سیکنڈ۔'),
    ('You can hear a blue whale’s heartbeat from more than 2 miles away.', 
     'آپ نیلے وہیل کے دل کی دھڑکن 2 میل سے زیادہ دور سے سن سکتے ہیں۔'),
    ('A single strand of spaghetti is called a "spaghetto."', 
     'ایک پتا سپیگٹی کو "اسپیگھیٹو" کہا جاتا ہے۔'),
    ('Elephants can’t jump.', 
     'ہاتھی چھلانگ نہیں لگا سکتے۔'),
    ('The shortest war in history lasted just 38 to 45 minutes.', 
     'تاریخ کی سب سے چھوٹی جنگ صرف 38 سے 45 منٹ تک جاری رہی۔'),
    ('There are more than 1,500 different types of bananas.', 
     'کیلے کی 1,500 سے زیادہ مختلف اقسام ہیں۔'),
    ('The unicorn is Scotland’s national animal.', 
     'یونیکورن اسکاٹ لینڈ کا قومی جانور ہے۔'),
    ('A "moment" technically refers to 90 seconds.', 
     'ایک "لمحہ" تکنیکی طور پر 90 سیکنڈ کو ظاہر کرتا ہے۔'),
    ('The majority of your brain is fat.', 
     'آپ کے دماغ کا زیادہ تر حصہ چربی پر مشتمل ہوتا ہے۔'),
    ('Hot water freezes faster than cold water, a phenomenon known as the Mpemba effect.', 
     'گرم پانی ٹھنڈے پانی سے تیزی سے جم جاتا ہے، جو کہ امپیمبا اثر کے نام سے جانا جاتا ہے۔'),
    ('Peanuts are not nuts; they are legumes.', 
     'مونگ پھلی گری دار میوے نہیں ہے؛ یہ پھلیاں ہیں۔'),
    ('The heart of a shrimp is located in its head.', 
     'جھینگے کا دل اس کے سر میں ہوتا ہے۔'),
    ('Polar bear skin is black.', 
     'پولر بیئر کی جلد کالا رنگت کی ہوتی ہے۔'),
    ('Dolphins have names for each other.', 
     'ڈولفن ایک دوسرے کے لئے نام رکھتے ہیں۔'),
    ('The longest place name in the world has 85 letters.', 
     'دنیا کا سب سے لمبا مقام کا نام 85 حروف پر مشتمل ہے۔'),
    ('Kangaroos can’t walk backward.', 
     'کینگرو پیچھے نہیں چل سکتے۔'),
    ('The human nose can detect over 1 trillion different scents.', 
     'انسان کی ناک ایک کھرب سے زیادہ مختلف بووں کو پہچان سکتی ہے۔'),
    ('Venus is the hottest planet in our solar system.', 
     'زہرہ ہمارے شمسی نظام کا سب سے گرم سیارہ ہے۔'),
    ('An octopus’s brain is shaped like a donut.', 
     'آکٹوپس کا دماغ ڈونٹ کی شکل کا ہوتا ہے۔'),
    ('More than 80% of the ocean is unexplored.', 
     'سمندر کا 80% سے زیادہ حصہ غیر دریافت شدہ ہے۔'),
    ('The dot over the letters “i” and “j” is called a “tittle.”', 
     'حروف “i” اور “j” کے اوپر نقطہ کو “ٹٹِل” کہا جاتا ہے۔'),
    ('The human body has around 206 bones.', 
     'انسانی جسم میں تقریباً 206 ہڈیاں ہوتی ہیں۔'),
    ('There are about 200 distinct types of tomatoes.', 
     'ٹماٹروں کی تقریباً 200 مختلف اقسام ہیں۔'),
    ('A snail can sleep for three years.', 
     'سلاگ تین سال تک سو سکتا ہے۔'),
    ('Pineapples take about two years to grow.', 
     'انناس کو بڑھنے میں تقریباً دو سال لگتے ہیں۔'),
    ('A giraffe’s tongue is black.', 
     'جراف کی زبان کالا رنگت کی ہوتی ہے۔'),
    ('Cows have best friends and can become stressed when separated.', 
     'گائے کے بہترین دوست ہوتے ہیں اور الگ ہونے پر ان میں تناؤ ہو سکتا ہے۔'),
    ('In Japan, there is a museum dedicated entirely to rocks that look like faces.', 
     'جاپان میں ایک میوزیم ہے جو مکمل طور پر چٹانوں کے لئے وقف ہے جو چہرے کی طرح دکھائی دیتے ہیں۔'),
    ('A “Baker’s dozen” means 13 items, not 12.', 
     'ایک "بیکر کا درجن" 13 اشیاء کا مطلب ہے، 12 نہیں۔'),
    ('The average person walks the equivalent of five times around the world in their lifetime.', 
     'عام آدمی اپنی زندگی میں دنیا کے پانچ بار چکر لگانے کے برابر چلتا ہے۔'),
    ('The Great Wall of China is not visible from the Moon with the naked eye.', 
     'چین کی عظیم دیوار چاند سے ننگی آنکھ سے نظر نہیں آتی۔'),
    ('A group of pandas is called an “embarrassment.”', 
     'پینڈاس کے گروپ کو "شرمندگی" کہا جاتا ہے۔'),
    ('One light year is about 5.88 trillion miles.', 
     'ایک روشنی سال تقریباً 5.88 کھرب میل ہے۔'),
    ('A “murder” is a group of crows.', 
     'ایک "قتل" کو ایک گروپ کی شکل میں کالے کوا کہا جاتا ہے۔'),
    ('The human eye can distinguish about 10 million different colors.', 
     'انسان کی آنکھ تقریباً 10 ملین مختلف رنگوں کو ممتاز کر سکتی ہے۔'),
    ('A baby octopus is the size of a flea when it is born.', 
     'ایک نیا پیدا ہونے والا آکٹوپس مچھر کے برابر ہوتا ہے۔')
]




# Function to get a random fun fact and its Urdu translation
def get_fun_fact():
    fact = random.choice(fun_facts)
    return fact

# Streamlit application code
st.set_page_config(page_title="Student Fun App", page_icon=":tada:")

# Add CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/earlyaccess/notonastaliqurdudraft.css');

        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            color: #333;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            color: #4CAF50;
            margin-top: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .fact {
            font-size: 22px;
            color: #444;
            margin-bottom: 20px;
            background: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s ease-in-out;
        }
        .fact:hover {
            transform: scale(1.02);
        }
        .urdu-text {
            font-family: 'Noto Nastaliq Urdu Draft', serif;
            font-size: 22px;
            background: #fafafa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s ease-in-out;
        }
        .urdu-text:hover {
            transform: scale(1.02);
        }
        .footer {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-top: 50px;
        }
        .footer a {
            color: #1E90FF;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Welcome to the Student Fun App!</div>', unsafe_allow_html=True)

# Initialize session state to store the current fact
if 'fact' not in st.session_state:
    st.session_state.fact = get_fun_fact()

# Display fun fact
if st.button("Get Fun Fact"):
    st.session_state.fact = get_fun_fact()

english_fact, urdu_fact = st.session_state.fact
st.markdown(f'<div class="fact">{english_fact}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="urdu-text">{urdu_fact}</div>', unsafe_allow_html=True)


# Footer
st.markdown("""
    <div class="footer">
        Developed By: Irfan Ullah Khan<br>
        <a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a><br>
        Developed For: Essential Generative AI Training<br>
        Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN
    </div>
""", unsafe_allow_html=True)
