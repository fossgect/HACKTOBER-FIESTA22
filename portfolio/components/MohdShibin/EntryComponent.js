import Image from "next/image";
import PortfolioNavbar from "./Navbar/Navbar";
import ProfileImg from '../../public/MohdShibin.jpg'
import { useEffect, useState } from "react";
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react";


export default function EntryComponent() {

    const [txt, setTxt] = useState("Hola I'm Shibin")
    var i = 0;
    var speed = 100;

    function typeWriter() {
        if (i < txt.length) {
            document.getElementById("typeTxt").innerHTML += txt.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
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
                        An undergraduate computer science student from india.<br />
                        <br /><br />
                        {/* Add Your Tech Stacks */}
                        Tech Stacks : JavaScript, Flutter, Django, Nodejs
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
                                <Text b>Piano App</Text>
                            </Card.Header>
                            <Card.Divider />
                            <Card.Body css={{ py: "$10" }}>
                                <Text>
                                    A light weight piano mobile application developed using Flutter
                                </Text>
                            </Card.Body>
                            <Card.Divider />
                            <Card.Footer>
                                <Row justify="flex-end">
                                    <Link href="https://github.com/MohdShibin/Piano-App">
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
                                <Text b>LibPro</Text>
                            </Card.Header>
                            <Card.Divider />
                            <Card.Body css={{ py: "$10" }}>
                                <Text>
                                    A library management system developed using Java and Mysql
                                </Text>
                            </Card.Body>
                            <Card.Divider />
                            <Card.Footer>
                                <Row justify="flex-end">
                                    <Link href="https://github.com/MohdShibin/Libpro">
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
                                <Text b>Snake Game</Text>
                            </Card.Header>
                            <Card.Divider />
                            <Card.Body css={{ py: "$10" }}>
                                <Text>
                                    A simple snake game using Python.
                                </Text>
                            </Card.Body>
                            <Card.Divider />
                            <Card.Footer>
                                <Row justify="flex-end">
                                    <Link href="https://github.com/fossgect/HACKTOBER-FIESTA22/blob/main/pygame/gameit/MohdShibin.py">
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
