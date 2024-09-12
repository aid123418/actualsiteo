import streamlit
import streamlit as st


st.title("Welcome to SCP: Roleplay server, Site Ω furry containment")
st.subheader("Site Ω furry containment is a WIP server in the roblox game SCP: Roleplay by Tea_TimeToday1.")


col1, col2 = st.columns(2)

with col1:
    st.write("Hello! A little about me: I joined on a account origionaly from 2014 and sadly lost that one."
                   " I now have 2 accounts, aid123418 (my old, mostly unused) And Tea_timetoday1. Im using my main account to create this server-"
                   " as i have been intruiged on people making awesome custom servers. ")
    st.link_button(url="https://www.roblox.com/games/5041144419/SCP-Roleplay", label="SCP: Roleplay link")
    st.image('images/webp.webp')

with col2:
    st.write ("You may find our communications server, and the link to SCP: Roleplay. The Links are below."
              "If you are here for the applications- Please click the Applicatons and and the name application you want to do."
              " If you are here to contact me. Use the info on the contact info tab. The rules are on the rules tab as usual. ")
    st.link_button(url="https://discord.com/invite/TgAvQNGubx", label="Site Ω Communications")
    st.image('images/omega.jpeg')


tab1, tab2, tab3 = st.tabs(["Applications", "Contact Info", "Rules"])


with tab1:
     link = st.link_button(url="https://forms.gle/qVoMNz83RopkrDsR7", label="Ω-1 Application")
     link2 = st.link_button(url="https://docs.google.com/forms/d/e/1FAIpQLScHBXF8NphwUVtHxTCdte0q88B4e-yUFiyGPT4lrt8vqc1PTQ/viewform?usp=sf_link", label="Moderator Application")

with tab2:
    st.info("Contact Tea_Timetoday1. His discord @ is @aid123418. if you need to email Tea, all emails can be sent to waitwhahappened@gmail.com.")
    st.link_button(url="https://mail.google.com/mail/u/0/#inbox", label="Link to G-mail")

with tab3:
    if st.button('Rules and Guide to site Ω')
        st.link_button(url="https://roblox.com/home", label="Roblox TOS")
        st.link_button(url="https://roblox.com/home", label="Site Ω Rules")
