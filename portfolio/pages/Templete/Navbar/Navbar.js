import { Navbar, Link, Text, Avatar, Dropdown } from "@nextui-org/react";
import { Layout } from "./Layout.js";

export default function PortfolioNavbar() {

  return (
    <Layout>
      <Navbar isBordered variant="sticky">
        <Text b color="inherit" className="nav-heading" >
            Portfolio
        </Text>
        <Navbar.Brand
          css={{
            "@xs": {
              w: "12%",
            },
          }}
        >
          <Text b color="inherit" hideIn="xs">
            Portfolio
          </Text>
        </Navbar.Brand>
        <Navbar.Content
          css={{
            "@xs": {
              w: "12%",
              jc: "flex-end",
            },
          }}
        >
          <Dropdown placement="bottom-right">
            <Navbar.Item>
                <Avatar
                  bordered
                  as="button"
                  color="secondary"
                  size="md"
                  src="/Template.jpg" // Change Image name to your Uploaded File Name
                />
            </Navbar.Item>
          </Dropdown>
        </Navbar.Content>
      </Navbar>
    </Layout>
  );
}
