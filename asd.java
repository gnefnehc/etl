package com.example.tests;

import com.thoughtworks.selenium.Selenium;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver;
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.regex.Pattern;
import static org.apache.commons.lang3.StringUtils.join;

public class asd {
	private Selenium selenium;

	@Before
	public void setUp() throws Exception {
		WebDriver driver = new FirefoxDriver();
		String baseUrl = "https://developers.facebook.com/tools/explorer/";
		selenium = new WebDriverBackedSelenium(driver, baseUrl);
	}

	@Test
	public void testAsd() throws Exception {
		selenium.open("/tools/explorer/#");
		selenium.click("//div[@id='js_6']/div/ul/li[4]/a/span/span/span");
		selenium.click("css=#js_7 > span._55pe");
		selenium.click("css=span._2nax");
		selenium.click("xpath=(//button[@value='1'])[5]");
		selenium.waitForPopUp("_blank", "30000");
		selenium.click("//div[@id='u_0_0']/div/div[2]/div/div[2]/a/span");
		selenium.click("//div[@id='js_7']/div/ul/li[6]/a/span/span/span");
		selenium.waitForPopUp("_blank", "30000");
		selenium.selectWindow("null");
		selenium.click("id=u_0_2");
		selenium.selectWindow("name=_e_0IWn");
		selenium.click("css=span._54nh");
		selenium.waitForPageToLoad("30000");
		selenium.selectWindow("name=_e_0IWn");
		selenium.click("id=u_0_3");
		selenium.waitForPageToLoad("30000");
		selenium.selectWindow("name=_e_0LQv");
		selenium.click("//div[@id='js_7']/div/ul/li[4]/a/span/span/span");
		selenium.click("css=#js_8 > span._55pe");
		selenium.click("//div[@id='js_a']/div/ul/li[4]/a/span/span/span");
		selenium.waitForPopUp("_blank", "30000");
		selenium.selectWindow("name=_e_0jYR");
		selenium.type("id=pass", "ji3rul4tp6z");
		selenium.type("id=email", "www_love_you_to@yahoo.com.tw");
		selenium.click("id=u_0_2");
		selenium.waitForPageToLoad("30000");
		selenium.click("id=u_0_4");
		selenium.click("css=span._5kx5");
		selenium.click("id=u_0_2");
		selenium.click("css=span._54nh");
		selenium.waitForPageToLoad("30000");
		selenium.type("id=pass", "ji3rul4tp6z");
		selenium.type("id=email", "www_love_you_to@yahoo.com.tw");
		selenium.click("id=u_0_2");
		selenium.waitForPageToLoad("30000");
		selenium.click("name=__CONFIRM__");
	}

	@After
	public void tearDown() throws Exception {
		selenium.stop();
	}
}
