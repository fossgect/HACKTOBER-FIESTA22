import Image from "next/image"
import PortfolioNavbar from "./Navbar/Navbar"
import ProfileImg from '../../public/sai-na.jpg' // Change Image name to your Uploaded File Name
import { useEffect, useState } from "react"
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react"


export default function EntryComponent() {



    const [txt, setTxt] = useState("Hey I'm SAI NATH A") // Change X to Your Full Name

    var i = 0
    var speed = 100

    function typeWriter() {
        if (i < txt.length) {
            document.getElementById("typeTxt").innerHTML += txt.charAt(i)
            i++
            setTimeout(typeWriter, speed)
        }
    }

    useEffect(() => {
        typeWriter()
        setTxt("")
    })

    return (
        <div className="">

            {/* Navbar */}
            <PortfolioNavbar />

            {/* Hero Section */}
            <div className="w-full flex flex-col items-center py-16 px-8">
                {/* Profile Image */}





                <div className="w-fit h-fit max-w-[200px] max-h-[200px] border p-1 border-black rounded-[50%]">

                    <Image src={ProfileImg} style={{ borderRadius: "50%", margin: "0" }} />
                </div>
                {/* Description */}
                <div className="description mt-6">
                    <div >
                        <h1 id="typeTxt" className="font-txt text-xl font-extrabold text-center"></h1>
                    </div>
                    <p className="text-center font-txt mt-3 max-w-[600px]">
                        {/* Change Description Here */}
                        I am 2nd year computer science and engineering student of Government Engineering College,Thrissur., <br />
                        I have also 3 year diploma in computer engineering
                        I am interested in  AI , ML , React JS.
                        <br /><br />
                        {/* Add Your Tech Stacks */}
                        Tech Stacks : React JS , Firebase , nodeJS
                    </p>
                </div>
            </div>

            {/* Project Section */}
            <div className="w-full pb-8 flex justify-center">

                {/* <h1 className="text-center font-bold text-2xl">Projects</h1> */}




                <div className="max-w-sm rounded-lg overflow-hidden shadow-lg font-sans">
                    <img className="w-full " src="https://firebasestorage.googleapis.com/v0/b/linux-gec.appspot.com/o/pygame-sai-na.png?alt=media&token=dc3188f8-bc7f-411a-b0cf-09a47131dc61" alt="Sunset in the mountains" />
                    <div className="px-6 py-4">
                        <div className="font-bold text-2xl mb-2 font-sans">Halloween Hunt 🎃</div>
                        <p className="text-gray-700 text-lg font-sans mt-4">
                            Halloween Hunt 🎃 is a simple game created using python. The aim of th game is collect many pumpkins 🎃 as you can without contact with enemy 🤖 ,  Whenever the player got contacted to enemy, he'll loose a life ♥  . After loosing three lives
                        </p>
                    </div>
                    <div className="px-6 pt-4 pb-2">
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#pygame</span>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#Halloween</span>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#HACKTOBER-FIESTA22</span>
                    </div>
                </div>


            </div>
        </div>
    )
}
