import Image from "next/image";
import PortfolioNavbar from "./Navbar/Navbar";
import ProfileImg from '../../public/majid-2002.jpg' // Change Image name to your Uploaded File Name
import { useEffect, useState } from "react";
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react";


export default function EntryComponent(){

    const [txt,setTxt] = useState("Hey I'm Majid") // Change X to Your Full Name

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
                        I am a full stack Web developer and student in computer science pursuing Btech from Government Engineering College, Thrissur
                        <br/><br/>
                        {/* Add Your Tech Stacks */}
                        Tech Stacks : HTML, CSS, JavaScript, Node.JS, MongodDB, React.JS
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
                            <Text b>JumpMan Game</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                JumpMan game using python pygame library
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/fossgect/HACKTOBER-FIESTA22/blob/main/pygame/gameit/majid_2002.py">
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
                            <Text b>Personal Web for Client</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                A personal website for a client
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/majid-2002/Marzooq-Static-Website">
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
                            <Text b>TinDog</Text>
                        </Card.Header>
                        <Card.Divider />
                        <Card.Body css={{ py: "$10" }}>
                            <Text>
                                A tinder for Dogs Website
                            </Text>
                        </Card.Body>
                        <Card.Divider />
                        <Card.Footer>
                            <Row justify="flex-end">
                                <Link href="https://github.com/majid-2002/TinDog-Start">
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
