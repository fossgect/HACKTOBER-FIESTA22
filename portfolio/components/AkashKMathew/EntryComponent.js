import Image from "next/image";
import PortfolioNavbar from "./Navbar/Navbar";
import ProfileImg from '../../public/AkashKMathew.jpg'
import { useEffect, useState } from "react";
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react";


export default function EntryComponent(){

    const [txt,setTxt] = useState("Hey I'm Akash")

    var i = 0;
    var speed = 100;

    function typeWriter() {
    if (i < txt.length) {
        document.getElementById("typeTxt").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
    }

    useEffect(()=>{
        typeWriter()
        setTxt("")
    })

    return(
        <div className="">

            {}  
            <PortfolioNavbar/>

            {}
            <div className="w-full flex flex-col items-center py-16 px-8">
                {}
                <div className="w-fit h-fit max-w-[200px] max-h-[200px] border p-1 border-black rounded-[50%]">
                    <Image src={ProfileImg} style={{borderRadius: "50%",margin: "0"}} />
                </div>
                {}
                <div className="description mt-6">
                    <div >
                        <h1 id="typeTxt" className="font-txt text-xl font-extrabold text-center"></h1>
                    </div>
                    <p className="text-center font-txt mt-3 max-w-[600px]">
                        {}
                        I am currently persuing computer science engineering at GEC Thrissur. Coding is an endless process of trial and error. Sometimes the code fails and it often takes many, many tries until that magical moment when what we are trying to build comes to life. These moments make me more happier.
                        <br/><br/>
                        {}
                        Tech Stacks : Python, C, C++, Java, HTML, CSS, JavaScript, Flutter, etc
                    </p>
                </div>
            </div>

            
        </div>
    )
}
