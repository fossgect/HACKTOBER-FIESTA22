import Image from "next/image";
import PortfolioNavbar from "./Navbar/Navbar";
import ProfileImg from "../../public/Prometheus2k.jpg"; // Change Image name to your Uploaded File Name
import { useEffect, useState } from "react";
import { Card, Grid, Text, Row, Button, Link } from "@nextui-org/react";

export default function EntryComponent() {
  const [txt, setTxt] = useState("Hey I'm X"); // Change X to Your Full Name

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
    typeWriter();
    setTxt("");
  });

  return (
    <div className="">
      {/* Navbar */}
      <PortfolioNavbar />

      {/* Hero Section */}
      <div className="w-full flex flex-col items-center py-16 px-8">
        {/* Profile Image */}
        <div className="w-fit h-fit max-w-[200px] max-h-[200px] border p-1 border-black rounded-[50%]">
          <Image
            src={ProfileImg}
            style={{ borderRadius: "50%", margin: "0" }}
          />
        </div>
        {/* Description */}
        <div className="description mt-6">
          <div>
            <h1
              id="typeTxt"
              className="font-txt text-xl font-extrabold text-center"
            ></h1>
          </div>
          <p className="text-center font-txt mt-3 max-w-[600px]">
            {/* Change Description Here */}
            App Developer | Web developer | web3 enthusiast
            <br />
            <br />
            {/* Add Your Tech Stacks */}
            Tech Stacks : HTML, CSS, JavaScript, Flutter, ReactJs, Firebase,
            Solidity
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
                <Text b>2048 Game</Text>
              </Card.Header>
              <Card.Divider />
              <Card.Body css={{ py: "$10" }}>
                <Text>
                  This game is developed using pygame and numpy. Those who
                  reaches the number 2048 wins.
                </Text>
              </Card.Body>
              <Card.Divider />
              <Card.Footer>
                <Row justify="flex-end">
                  <Link href="https://github.com/Prometheus2k/2048-Game">
                    <Button size="sm" light color="primary">
                      Link
                    </Button>
                  </Link>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>

          {/* Project 2 */}
          <Grid sm={12} md={5} className="flex justify-center">
            <Card css={{ width: "330px" }}>
              <Card.Header>
                <Text b>NxtVote</Text>
              </Card.Header>
              <Card.Divider />
              <Card.Body css={{ py: "$10" }}>
                <Text>
                  A Blockchain voting system for college elections based on
                  smart contracts leveraging the power and security of Ethereum
                  blockchain.
                </Text>
              </Card.Body>
              <Card.Divider />
              <Card.Footer>
                <Row justify="flex-end">
                  <Link href="https://github.com/Prometheus2k/smart-vote">
                    <Button size="sm" light color="primary">
                      Link
                    </Button>
                  </Link>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>

          {/* Project 3 */}
          <Grid sm={12} md={5} className="flex justify-center">
            <Card css={{ width: "330px" }}>
              <Card.Header>
                <Text b>SAE club website</Text>
              </Card.Header>
              <Card.Divider />
              <Card.Body css={{ py: "$10" }}>
                <Text>
                  This is a website developed for SAE club of GEC Thrissur.
                </Text>
              </Card.Body>
              <Card.Divider />
              <Card.Footer>
                <Row justify="flex-end">
                  <Link href="https://sae.gectcr.ac.in">
                    <Button size="sm" light color="primary">
                      Link
                    </Button>
                  </Link>
                </Row>
              </Card.Footer>
            </Card>
          </Grid>
        </div>
      </div>
    </div>
  );
}
