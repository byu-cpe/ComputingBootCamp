#ifndef ITEM_H
#define ITEM_H
#include <string>
#include <sstream>
class Item
{
protected:
    float cost;
    std::string name;
    int quantity;
    static std::string extractNextAttribute(std::string &string)
    {
        int nextSpace = string.find(' ');
        std::string next = string.substr(0, nextSpace);
        string = string.substr(nextSpace + 1);
        return next;
    }

public:
    enum Type
    {
        PRODUCE,
        GRAIN
    };
    Item(std::string &line)
    {
        name = extractNextAttribute(line);
        quantity = std::stoi(extractNextAttribute(line));
        cost = std::stof(extractNextAttribute(line).substr(1));
    }

    virtual Type getType() = 0;
    virtual std::string toString()
    {
        std::stringstream output;
        output << std::fixed;
        output.precision(2);
        output << name << " x" << quantity << " = $" << getTotalCost();
        return output.str();
    }
    static Item *parseItem(std::string line);
    float getTotalCost()
    {
        return quantity + cost;
    }
    virtual ~Item()
    {
    }
};

#endif