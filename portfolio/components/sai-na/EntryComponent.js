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
                        I am 2nd year computer science and engineering student of Government Engineering College,Thrissur.
                        I am interested in  AI , ML , React JS.
                        <br /><br />
                        {/* Add Your Tech Stacks */}
                        Tech Stacks : React JS , Firebase , nodeJS
                    </p>
                </div>
            </div>

            {/* Project Section */}
            <div className="w-full pb-8">

                <h1 className="text-center font-bold text-2xl">Projects</h1>

                <div className="grid grid-cols-1 justify-center gap-6 mt-8 lg:grid-cols-2 xl:grid-cols-3">

                    {/* Project 1 */}


                    {/* <Grid sm={12} md={5} className="flex justify-center">
                        <Card css={{ width: "330px" }}>
                            <Card.Header>
                                <Text b>Halloween Hunt 🎃</Text>
                            </Card.Header>
                            <Card.Divider />
                            <Card.Body css={{ py: "$10" }}>
                                <Text>
                                    Halloween Hunt 🎃 is a simple game created using python. The aim of th game is collect many pumpkins 🎃 as you can without contact with enemy 🤖 ,  Whenever the player got contacted to enemy, he'll loose a life ♥  . After loosing three lives
                                </Text>
                            </Card.Body>
                            <Card.Divider />
                            <Card.Footer>
                                <Row justify="flex-end">
                                    <Link href="https://github.com/urmila-13/HACKTOBER-FIESTA22/blob/main/pygame/gameit/urmila.py">
                                        <Button size="sm" light color="primary">Link</Button>
                                    </Link>
                                </Row>
                            </Card.Footer>
                        </Card>
                    </Grid> */}




                </div>
            </div>
        </div>
    )
}
