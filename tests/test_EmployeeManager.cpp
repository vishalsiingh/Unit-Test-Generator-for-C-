#include <gtest/gtest.h>
#include "../cpp_project/EmployeeManager.h"

class EmployeeManagerTest : public ::testing::Test {
protected:
    EmployeeManager manager;
};

TEST_F(EmployeeManagerTest, AddPositive) {
    EXPECT_EQ(manager.add(2, 3), 5);
}

TEST_F(EmployeeManagerTest, AddNegative) {
    EXPECT_EQ(manager.add(-5, -3), -8);
}

TEST_F(EmployeeManagerTest, GreetUser) {
    EXPECT_EQ(manager.greet("Vishal"), "Hello, Vishal");
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
