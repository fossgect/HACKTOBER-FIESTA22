import Image from "next/image";
import PortfolioNavbar from "./Navbar/Navbar";
import ProfileImg from '../../public/anuragrajanp.jpg' // Change Image name to your Uploaded File Name
import { useEffect, useState } from "react";
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react";


export default function EntryComponent(){

    const [txt,setTxt] = useState("Hey I'm Anurag P") // Change X to Your Full Name

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

            {/* Navbar */}  
            <PortfolioNavbar/>

            {/* Hero Section */}
            <div className="w-full flex flex-col items-center py-16 px-8">
                {/* Profile Image */}
                <div className="w-fit h-fit max-w-[200px] max-h-[200px] border p-1 border-black rounded-[50%]">
                    <Image src={ProfileImg} style={{borderRadius: "50%",margin: "0"}} />
                </div>
                {/* Description */}
                <div className="description mt-6">
                    <div >
                        <h1 id="typeTxt" className="font-txt text-xl font-extrabold text-center"></h1>
                    </div>
                    <p className="text-center font-txt mt-3 max-w-[600px]">
                        {/* Change Description Here */}
                        CSE undergrad | Govt Engineering College, Thrissur
                        <br/><br/>
                        {/* Add Your Tech Stacks */}
                        Tech Stacks : HTML, CSS, JavaScript, Flutter
                    </p>
                </div>
            </div>

            {/* Project Section */}
            <div className="w-full pb-8">

                <h1 className="text-center font-bold text-2xl">Projects</h1>

                <div className="grid grid-cols-1 justify-center gap-6 mt-8 lg:grid-cols-2 xl:grid-cols-3">

                    {/* Project 1 */}
                    <Grid sm={12} md={5} className="flex justify-center">
                        <Card css={{ width: "330px" }}>
                        <Card.Header>
                            <Text b>Medhelper</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                Personal Medical Assistant app developed using Flutter. It allows users to take medicines on regular intervals with information such as medicin neame, medicine type and dose. 
                                It also allows local medicine sellers to sell medicines to customers through the app and deliver to their doorsteps. The app also has a doctor login which allows doctors to meet patients through video conference.
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/anuragrajanp">
                                    <Button size="sm" light color="primary">Link</Button>
                                </Link>
                            </Row>
                        </Card.Footer>
                        </Card>
                    </Grid>

                    {/* Project 2 */}
                    <Grid sm={12} md={5} className="flex justify-center">
                        <Card css={{ width: "330px" }}>
                        <Card.Header>
                            <Text b>The Big Pig Game</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                <a href="https://anuragrajanp.github.io/TheBigPigGame">The Big Pig Game</a> is a simple multiplayer game developed using HTML, CSS and JavaScript.
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/anuragrajanp/TheBigPigGame">
                                    <Button size="sm" light color="primary">Link</Button>
                                </Link>
                            </Row>
                        </Card.Footer>
                        </Card>
                    </Grid>

                    {/* Project 3 */}
                    <Grid sm={12} md={5} className="flex justify-center">
                        <Card css={{ width: "330px" }}>
                        <Card.Header>
                            <Text b>YouTube Watchtime Calculator</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                It's a C++ program that calculates YouTube watchtime. Using this program we can calculate any of the watch time, views and duration of a video using the other two values. 
                                This program is used to calculate YouTube watch hour with the input of video duration and number of views considering that viewers watched 100% of the video.
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/anuragrajanp/watchtime">
                                    <Button size="sm" light color="primary">Link</Button>
                                </Link>
                            </Row>
                        </Card.Footer>
                        </Card>
                    </Grid>

                    
                </div>
            </div>
        </div>
    )
}
